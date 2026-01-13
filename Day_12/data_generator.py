# Day 12: Modules - Leveraging the Python Standard Library
# Modules allow us to use pre-written code to solve complex problems.

import math
import random

# 1. Using the 'random' module to simulate raw sensor data
def generate_synthetic_data(num_samples):
    data = []
    for _ in range(num_samples):
        # Simulating a value between 0 and 100
        data.append(random.uniform(0, 100))
    return data

# 2. Using the 'math' module for AI-related calculations
def calculate_loss_log(value):
    # Simulating a logarithmic loss calculation
    return math.log1p(value)

# --- Execution ---
samples = generate_synthetic_data(5)
print(f"Synthetic Data Samples: {samples}")

sample_loss = calculate_loss_log(samples[0])
print(f"Calculated Log Loss for Sample 1: {sample_loss:.4f}")
