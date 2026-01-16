# Day 16: Python Datetime - Performance Benchmarking
# Tracking training duration and versioning models with timestamps.

from datetime import datetime
import time

# 1. Capture Start Time
start_time = datetime.now()
print(f"🚀 Training started at: {start_time.strftime('%H:%M:%S')}")

# 2. Simulate a training delay (3 seconds)
print("...Training in progress...")
time.sleep(3)

# 3. Capture End Time
end_time = datetime.now()
duration = end_time - start_time

# 4. Generate a Versioned Filename
timestamp = end_time.strftime("%Y%m%d_%H%M")
model_filename = f"model_v2_{timestamp}.pkl"

print(f"✅ Training Complete. Duration: {duration.total_seconds()} seconds")
print(f"📦 Model saved as: {model_filename}")