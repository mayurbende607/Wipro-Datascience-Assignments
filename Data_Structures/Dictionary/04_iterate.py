# 4.Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.

dic = {1: "Apple", 2: "Banana", 3: "Mango"}

print("Keys:")
for key in dic:
    print(key)

print("Values:")
for value in dic.values():
    print(value)

print("Keys and Values:")
for key, value in dic.items():
    print(key, value)
