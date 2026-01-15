# Day 15: Python Type Errors - The Debugging Milestone
# Understanding how to read tracebacks and identify common ML data errors.

def process_model_input(value):
    # Intentional error: Adding a string to an integer
    # This will trigger a 'TypeError'
    return value + " is the score"

def check_list_index(data):
    # Intentional error: Accessing an index that doesn't exist
    # This will trigger an 'IndexError'
    return data[10]

# --- Practice Zone ---
print("🔍 Learning to identify errors...")

# 1. TypeError: Mixing data types
try:
    process_model_input(0.95)
except TypeError as e:
    print(f"❌ TypeError caught: {e}. (Reason: Cannot concatenate float and string)")

# 2. NameError: Using a variable that isn't defined
try:
    print("unknown_variable")
except NameError as e:
    print(f"❌ NameError caught: {e}. (Reason: Variable not initialized)")

# 3. ValueError: Incorrect values for functions
try:
    import math
    math.sqrt(-1)
except ValueError as e:
    print(f"❌ ValueError caught: {e}. (Reason: Math domain error)")

print("\n✅ Mastery of error identification is key to building fault-tolerant AI.")