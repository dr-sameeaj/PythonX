# Variables representing ML Model Parameters
developer_name = "Sameeraj"
model_name = "Neural Network v1"
learning_rate = 0.01
is_trained = False
epochs = 50
accuracy_score = 0.89

# Using built-in functions on data-like structures
print(type(learning_rate))  # Check if it's a float
print(len(model_name))      # Length of the string

# we can print a few things as follows

user_name = input("Hello, I am your Python AI. What is your name? ")
user_age = input(f"Nice to meet you, {user_name}. How old are you? ")

# Practicing type conversion (Day 2 concept)
years_to_hundred = 100 - int(user_age)
if (user_age>17):
  print("Adult")

print(f"Stats for {user_name}:")
print(f"Currently {user_age} years old. You will be 100 in {years_to_hundred} years!")
