# 6.Write a function that takes a number as a parameter and checks whether the number is prime or not.

def is_prime(num):

    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime")
else:
    print("Not Prime")
