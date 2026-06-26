# 5.Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive.

s = input("Enter a string: ")
n = int(input("Enter n: "))

last = s[-n:]

result = last * n

print(result)
