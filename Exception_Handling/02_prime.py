# 2.Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.

try:
    num = int(input("Enter a number: "))

    if num < 2:
        print("Not Prime")
    else:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print("Prime")
        else:
            print("Not Prime")

except ValueError:
    print("Error: Please enter a valid number")
