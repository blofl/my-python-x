# Simple Addition Calculator

# Prompt the user for the first number
first_number = input("Enter the first number: ")

# Prompt the user for the second number
second_number = input("Enter the second number: ")

# Convert the input strings to float numbers
num1 = float(first_number)
num2 = float(second_number)

# Add the two numbers together
result = num1 + num2

# Print the result in a friendly message
print(f"Great! {num1} + {num2} = {result}")