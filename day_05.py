# Day 5: Lists - Managing an AI Model Dataset
# In ML, we often store model performance scores in lists to analyze them.

# 1. Creating a List (A "Vector" of accuracy scores)
model_accuracies = [0.85, 0.92, 0.78, 0.95, 0.88]

# 2. Adding data (We trained a new model!)
model_accuracies.append(0.91)

# 3. Modifying data (Realizing a score was recorded incorrectly)
model_accuracies[2] = 0.80  # Changing 0.78 to 0.80

# 4. List Methods for Analysis
model_accuracies.sort(reverse=True)  # Sort from best to worst
best_score = model_accuracies[0]
worst_score = model_accuracies[-1]

# 5. Slicing the Top 3 Models
top_3_models = model_accuracies[:3]

print(f"Full Dataset: {model_accuracies}")
print(f"Top Performer: {best_score}")
print(f"Top 3 Models for Deployment: {top_3_models}")
