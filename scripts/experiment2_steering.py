"""Experiment 2: Taste Steering Vectors

Can we shift a model's research question generation by adding a "taste direction"
to its activations? This is the key test: if taste is linearly encoded, we should
be able to steer the model to generate in different research styles.

Method: Contrastive Activation Addition (CAA)
1. Compute mean activation for each taste style
2. Compute "taste direction" = mean(style_A) - mean(style_B)
3. Add scaled taste direction to model activations during generation
4. Compare generated text with and without steering
"""
import json, torch, numpy as np
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM
from collections import Counter
import sys

model_name = sys.argv[1] if len(sys.argv) > 1 else "Qwen3.5-9B"
model_path = f"/workspace/models/{model_name}"
RESULTS_DIR = Path("/workspace/research-taster/results")

# Load data and representations
with open("/workspace/research-taster/data/arxiv_papers.json") as f:
    all_data = json.load(f)

rc = Counter(d["researcher"] for d in all_data)
valid_r = {r for r, c in rc.items() if c >= 5}
data = [d for d in all_data if d["researcher"] in valid_r]

reps_data = np.load(str(RESULTS_DIR / f"reps_{model_name}.npz"))
layers = sorted([int(k.split("_")[1]) for k in reps_data.files])
representations = {l: reps_data[f"layer_{l}"] for l in layers}

# Compute taste centroids per style at best layer
# Best layer from exp1: layer 12 for 9B, layer 25 for 27B
best_layer = 12 if "9B" in model_name else 25
reps = representations[best_layer]

style_centroids = {}
for style in set(d["researcher_style"] for d in data):
    indices = [i for i, d in enumerate(data) if d["researcher_style"] == style]
    if len(indices) >= 10:
        style_centroids[style] = reps[indices].mean(axis=0)

print(f"Computed centroids for {len(style_centroids)} styles at layer {best_layer}")

# Compute steering vectors (taste directions)
# Key contrasts:
contrasts = [
    ("ml_creative", "ml_benchmark", "creative → benchmark"),
    ("ml_creative", "ml_safety", "creative → safety"),
    ("social_ai", "ml_creative", "social → creative"),
    ("alife", "ml_benchmark", "alife → benchmark"),
    ("machine_behavior", "ml_creative", "behavioral → creative"),
]

steering_vectors = {}
for style_a, style_b, name in contrasts:
    if style_a in style_centroids and style_b in style_centroids:
        direction = style_centroids[style_a] - style_centroids[style_b]
        # Normalize
        direction = direction / np.linalg.norm(direction)
        steering_vectors[name] = direction
        print(f"  {name}: computed (norm of raw diff: {np.linalg.norm(style_centroids[style_a] - style_centroids[style_b]):.2f})")

# Load model for generation
print(f"\nLoading {model_name} for steered generation...")
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path, trust_remote_code=True,
    dtype=torch.bfloat16, device_map="auto"
)
model.eval()

# Hook to add steering vector during generation
class SteeringHook:
    def __init__(self, direction, scale=5.0, layer_idx=None):
        self.direction = torch.tensor(direction, dtype=torch.bfloat16)
        self.scale = scale
        self.layer_idx = layer_idx
        self.handle = None
    
    def hook_fn(self, module, input, output):
        # output is typically (hidden_states, ...) or just hidden_states
        if isinstance(output, tuple):
            hidden = output[0]
            hidden = hidden + self.scale * self.direction.to(hidden.device)
            return (hidden,) + output[1:]
        else:
            return output + self.scale * self.direction.to(output.device)
    
    def attach(self, model):
        # Find the right layer to hook
        if hasattr(model, 'language_model'):
            lm = model.language_model
        elif hasattr(model, 'model'):
            lm = model.model
        else:
            lm = model
        
        if hasattr(lm, 'layers'):
            layer = lm.layers[self.layer_idx]
        elif hasattr(lm, 'decoder') and hasattr(lm.decoder, 'layers'):
            layer = lm.decoder.layers[self.layer_idx]
        else:
            raise ValueError(f"Cannot find layers in {type(lm)}")
        
        self.handle = layer.register_forward_hook(self.hook_fn)
        return self
    
    def remove(self):
        if self.handle:
            self.handle.remove()

# Generation prompt
PROMPT = """You are a researcher. Generate a research question about the following topic.

Topic: How large language models develop and represent internal world models.

Research question:"""

def generate(model, tokenizer, prompt, max_tokens=200):
    messages = [{"role": "user", "content": prompt}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_tokens, temperature=0.7, do_sample=True, top_p=0.9)
    return tokenizer.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)

# Generate baseline
print("\n" + "="*70)
print("BASELINE (no steering)")
print("="*70)
for i in range(3):
    rq = generate(model, tokenizer, PROMPT)
    print(f"\n  [{i+1}] {rq.strip()[:300]}")

# Generate with each steering vector at different scales
results = {"model": model_name, "prompt": PROMPT, "steered": {}}

for name, direction in steering_vectors.items():
    print(f"\n{'='*70}")
    print(f"STEERING: {name}")
    print(f"{'='*70}")
    
    results["steered"][name] = {}
    
    for scale in [3.0, 5.0, 10.0]:
        print(f"\n  Scale={scale}:")
        hook = SteeringHook(direction, scale=scale, layer_idx=best_layer)
        hook.attach(model)
        
        generations = []
        for i in range(3):
            rq = generate(model, tokenizer, PROMPT)
            print(f"    [{i+1}] {rq.strip()[:300]}")
            generations.append(rq.strip())
        
        hook.remove()
        results["steered"][name][str(scale)] = generations

# Also try a different topic to test generalization
PROMPT2 = """You are a researcher. Generate a research question about the following topic.

Topic: The role of embodiment in artificial intelligence systems.

Research question:"""

print(f"\n{'='*70}")
print("TOPIC 2: Embodiment in AI")
print("="*70)

print("\n  Baseline:")
for i in range(2):
    rq = generate(model, tokenizer, PROMPT2)
    print(f"    [{i+1}] {rq.strip()[:300]}")

for name in ["creative → benchmark", "social → creative"]:
    if name in steering_vectors:
        print(f"\n  Steered ({name}, scale=5.0):")
        hook = SteeringHook(steering_vectors[name], scale=5.0, layer_idx=best_layer)
        hook.attach(model)
        for i in range(2):
            rq = generate(model, tokenizer, PROMPT2)
            print(f"    [{i+1}] {rq.strip()[:300]}")
        hook.remove()

# Save
out = RESULTS_DIR / f"exp2_steering_{model_name}.json"
with open(out, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {out}")
print("\nDONE")
