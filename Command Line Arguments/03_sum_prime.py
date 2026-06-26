 # 3.Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

import sys

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

total = 0

for i in range(1, 11):
    num = int(sys.argv[i])

    if is_prime(num):
        total += num

print("Sum of Prime Numbers =", total)
