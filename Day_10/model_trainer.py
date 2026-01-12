# Day 10: Loops - Simulating Model Training Epochs
# Loops allow us to automate repetitive tasks, like training cycles.

import time

# 1. Simulating a Training Loop (for loop)
print("🚀 Starting Model Training...")
accuracies = [0.65, 0.72, 0.78, 0.85, 0.91]

# In ML, one full pass over the dataset is an 'Epoch'
for epoch, acc in enumerate(accuracies, 1):
    print(f"Epoch {epoch}: Accuracy = {acc * 100}%")
    time.sleep(0.5)  # Simulating processing time

# 2. Monitoring Loss (while loop)
loss = 0.50
print("\n📉 Optimizing Loss...")
while loss > 0.05:
    print(f"Current Loss: {loss:.3f}")
    loss -= 0.10  # Simulating the optimizer reducing error

print("\n✅ Training Complete. Model optimized.")
