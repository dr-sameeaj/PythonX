# Day 8: Dictionaries - Mapping AI Model Parameters
# Dictionaries allow us to store data in structured Key-Value pairs.

# 1. Defining an AI Model Configuration
model_metadata = {
    "model_name": "VisionTransformer_v1",
    "accuracy": 0.89,
    "is_stable": True,
    "epochs": 50,
    "architecture": ["Input", "Hidden_Layer", "Output"]
}

# 2. Accessing and Updating Data
# Retrieving accuracy (Safe access using .get)
current_acc = model_metadata.get("accuracy")

# Updating a value after more training
model_metadata["accuracy"] = 0.92
model_metadata["epochs"] += 10

# 3. Adding new metadata (A "tag")
model_metadata["environment"] = "Production"

# 4. Extracting info for analysis
print(f"Tracking Model: {model_metadata['model_name']}")
print(f"Current Stats: {model_metadata}")