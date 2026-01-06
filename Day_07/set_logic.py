# Day 7: Sets - Data De-duplication for ML
# Sets are unordered collections of unique elements.

# 1. Simulating a messy list of dataset labels
raw_labels = ["Cat", "Dog", "Dog", "Bird", "Cat", "Cat", "Fish", "Dog"]

# 2. Using a Set to find unique categories (Classes)
unique_classes = set(raw_labels)

# 3. Adding a new class
unique_classes.add("Horse")

# 4. Checking if a specific class exists in our dataset
has_rabbit = "Rabbit" in unique_classes

print(f"Original Labels: {len(raw_labels)}")
print(f"Unique Classes identified: {unique_classes}")
print(f"Does dataset have 'Rabbit'? {has_rabbit}")