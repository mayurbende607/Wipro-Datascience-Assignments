# 4.Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.

try:
    numbers = [10, -5, 20, -3, 0, 15, -7, 8, 9, -1]

    index = int(input("Enter index (0-9): "))

    value = numbers[index]

    if value > 0:
        print("Positive number")
    elif value < 0:
        print("Negative number")
    else:
        print("Zero")

except IndexError:
    print("Error: Invalid index")
except ValueError:
    print("Error: Please enter a valid number")
