# Day 14: Higher Order Functions - AI Prediction Pipeline
# Using map, filter, and lambda to process model outputs.

# 1. Raw Prediction Confidence Scores (0.0 to 1.0)
predictions = [0.95, 0.42, 0.88, 0.30, 0.75, 0.98, 0.15]

# 2. FILTER: Keep only "High Confidence" predictions (above 0.70)
# We use a lambda function for a quick, one-line rule
high_confidence = list(filter(lambda x: x >= 0.70, predictions))

# 3. MAP: Format these scores into percentages for a UI
formatted_results = list(map(lambda x: f"{x * 100:.1f}%", high_confidence))

print(f"All Model Predictions: {predictions}")
print(f"Validated High-Confidence Scores: {high_confidence}")
print(f"User-Ready Format: {formatted_results}")

# 4. REDUCE (Bonus): Calculate the average confidence of high-confidence results
from functools import reduce
total_sum = reduce(lambda x, y: x + y, high_confidence)
average_conf = total_sum / len(high_confidence)

print(f"Average System Confidence: {average_conf:.2f}")