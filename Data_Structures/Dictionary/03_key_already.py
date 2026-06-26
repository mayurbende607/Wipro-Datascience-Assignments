# 3.Write a program to check if a given key already exists in a dictionary

dic = {1: "Apple", 2: "Banana", 3: "Mango"}

key = int(input("Enter key: "))

if key in dic:
    print("Key exists")
else:
    print("Key does not exist")
