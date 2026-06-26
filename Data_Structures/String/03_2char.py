# 3. Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2.

s = input("Enter a string: ")

first = s[:2]

result = first * len(s)

print(result)
