# 1. The Calculator App
# Objective: The aim of this assignment is to build a basic calculator 
# that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
# Task 3: Ensure your code can handle division by zero and other potential errors. 
# So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

# Create addition function
def addition(x, y):
    return x+y

# Create subtraction function
def subtraction(x,y):
    return x-y

# Create multiplication function
def multiplication(x, y):
    return x*y

# Create division function
def division(x,y):
    return x/y

# Ask for user's input on operation and the two numbers
operation = input("What operation would you like to perform (add/subtract/multiply/divide)? ").lower()
x = float(input("First number: "))
y = float(input("Second number: "))

# Depending on the input (add, subtract, multiply, divide), perform the operation and record result
if operation == "add":
    result = addition(x,y)
elif operation == "subtract":
    result = subtraction(x,y)
elif operation == "multiply": 
    result = multiplication(x,y)
elif operation == "divide":
    # If the second number is zero, record "Error" and alert the user that it results in error
    if y == 0: 
        result = "Error"
        print("You can't divide by zero!")
    else: result = division(x,y)
    # If the user didn't input a provided operation, record "Error" and alert the user
else: 
    result = "Error"
    print("Please try again and input one of the provided operations.")

# As long as the operation did not result in error, report the answer
if result != "Error": 
    print(f"Answer = {result}")