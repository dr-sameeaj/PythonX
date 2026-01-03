# Day 3: Operators - ML Logic Simulation
actual_value = 100
predicted_value = 95

# Arithmetic: Calculate the Error (Loss)
error = actual_value - predicted_value
error_margin = (error / actual_value) * 100

# Comparison: Is the prediction "Good Enough"?
is_accurate = error_margin < 10  # True if error is less than 10%

# Logical: Check for high confidence and accuracy
confidence_score = 0.92
ready_for_deployment = is_accurate and confidence_score > 0.90

print(f"Error Margin: {error_margin}%")
print(f"Is accurate? {is_accurate}")
print(f"Ready to deploy? {ready_for_deployment}")
