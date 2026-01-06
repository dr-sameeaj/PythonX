# Day 6: Tuples - Storing Immutable Model Configurations
# Tuples are perfect for data that should not be modified by the program.

# 1. Defining Model Hyperparameters (Immutable Configuration)
# (Learning_Rate, Batch_Size, Optimizer)
model_config = (0.001, 32, "Adam")

# 2. Storing Data Dimensions (Height, Width, Channels)
# Essential for Computer Vision tasks
input_shape = (224, 224, 3)

# 3. Accessing Data
print(f"Current Optimizer: {model_config[2]}")
print(f"Input Resolution: {input_shape[0]}x{input_shape[1]}")

# 4. Attempting to change a tuple (Uncomment to see the error)
# input_shape[0] = 128  # This will raise a TypeError
