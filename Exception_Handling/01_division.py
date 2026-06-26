# 1.Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result =", result)

except Exception as e:
    print("Error occurred:", e)
