# Day 13: List Comprehension - High-Speed Data Filtering
# List comprehensions provide a concise way to create and transform lists.

# 1. Simulating a raw dataset with 'noise' (values below 0 are errors)
raw_sensor_data = [22.5, -1.0, 45.3, -99.0, 30.1, 55.8, -5.0]

# 2. Traditional way (4 lines)
# cleaned_data = []
# for x in raw_sensor_data:
#     if x > 0:
#         cleaned_data.append(x)

# 3. The Pythonic way: List Comprehension (1 line)
# Logic: [expression for item in list if condition]
cleaned_data = [val for val in raw_sensor_data if val > 0]

# 4. Transforming data: Convert Celsius to Fahrenheit in one line
fahrenheit_data = [(val * 9/5) + 32 for val in cleaned_data]

print(f"Original: {raw_sensor_data}")
print(f"Cleaned (No Noise): {cleaned_data}")
print(f"Transformed (Fahrenheit): {fahrenheit_data}")