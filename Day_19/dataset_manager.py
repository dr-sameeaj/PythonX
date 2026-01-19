# Day 19: File Handling - Managing AI Datasets
# Reading JSON configurations and writing logs to TXT files.

import json
import os

# 1. Simulate a JSON dataset (often used for model configurations)
model_config = {
    "model_name": "Resilient_NLP_v1",
    "learning_rate": 0.001,
    "epochs": 50,
    "status": "ready"
}

# 2. WRITING: Save configuration to a .json file
with open("config.json", "w") as f:
    json.dump(model_config, f, indent=4)
    print("✅ Configuration saved to config.json")

# 3. READING: Load the configuration back
if os.path.exists("config.json"):
    with open("config.json", "r") as f:
        loaded_data = json.load(f)
        print(f"📂 Loaded Model: {loaded_data['model_name']}")

# 4. APPENDING: Log the activity to a .txt file
with open("training_logs.txt", "a") as log_file:
    log_file.write(f"Model {model_config['model_name']} loaded at {model_config['status']}\n")
    print("📝 Activity logged in training_logs.txt")