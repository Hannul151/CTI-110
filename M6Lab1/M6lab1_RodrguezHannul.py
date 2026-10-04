# Hannul Rodriguez
# 10/4/26  
# Lab 1
# Using ai to create a calculator that preforms basic arithmetic

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Error: Invalid operation.")
        return

    print("Result:", result)


calculator()