# Day 17: Exception Handling - Building Crash-Proof Pipelines
# Using try, except, and finally to handle unpredictable data.

def safe_divide_pixels(pixel_value):
    try:
        # Simulate a potential error (e.g., dividing by zero or wrong type)
        normalized = pixel_value / 255
        return round(normalized, 3)
    except ZeroDivisionError:
        print("⚠️ Error: Division by zero detected. Returning 0.0")
        return 0.0
    except TypeError:
        print(f"⚠️ Error: Invalid data type '{type(pixel_value).__name__}'. Skipping.")
        return None
    finally:
        # This runs no matter what
        pass

# --- Testing the Resilient Pipeline ---
raw_data = [255, 128, "corrupted_text", 0, 45]
processed_data = []

for item in raw_data:
    result = safe_divide_pixels(item)
    if result is not None:
        processed_data.append(result)

print(f"\n✅ Cleaned Data for Model: {processed_data}")