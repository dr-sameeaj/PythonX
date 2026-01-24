# Day 24: Statistics - Understanding Data Distribution
# Analyzing AI model performance using descriptive statistics.

import statistics

# 1. Simulated Dataset: Accuracy scores from 10 different model versions
accuracy_scores = [0.85, 0.88, 0.92, 0.78, 0.85, 0.90, 0.95, 0.82, 0.85, 0.89]

# 2. Calculating Central Tendency
mean_acc = statistics.mean(accuracy_scores)    # The average performance
median_acc = statistics.median(accuracy_scores) # The middle value (outlier resistant)
mode_acc = statistics.mode(accuracy_scores)     # The most frequent score

# 3. Calculating Variation (How much the performance fluctuates)
st_dev = statistics.stdev(accuracy_scores)

print("📊 AI Model Performance Report")
print(f"Average Accuracy (Mean): {mean_acc:.2f}")
print(f"Middle Performance (Median): {median_acc:.2f}")
print(f"Common Score (Mode): {mode_acc:.2f}")
print(f"Performance Fluctuation (Std Dev): {st_dev:.4f}")

# 4. Logical Check: Is the model stable?
if st_dev < 0.05:
    print("✅ Result: Model training is stable.")
else:
    print("⚠️ Warning: High variance in training results.")