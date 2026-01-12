# Day 11: Functions - Building an AI Data Pipeline
# Functions make code reusable, organized, and professional.

# 1. Defining a function to normalize data
# In ML, we often scale values between 0 and 1
def normalize_pixel_values(pixels):
    normalized = []
    for p in pixels:
        normalized.append(round(p / 255.0, 3))
    return normalized

# 2. Defining a function to check model readiness
def check_deployment_ready(accuracy, threshold=0.90):
    if accuracy >= threshold:
        return True
    return False

# --- Using the Functions ---
raw_data = [255, 128, 0, 45, 200]
processed_data = normalize_pixel_values(raw_data)

acc = 0.94
is_ready = check_deployment_ready(acc)

print(f"Processed Tensors: {processed_data}")
print(f"Ready for Production? {'Yes' if is_ready else 'No'}")
