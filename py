# Calculator for only 10 and 5

num1 = 10
num2 = 5

# Ask the user for the operator
operator = input("Enter an operator (+, -, *, /): ")

# Perform operation
if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operator. Please use +, -, *, or /.")
