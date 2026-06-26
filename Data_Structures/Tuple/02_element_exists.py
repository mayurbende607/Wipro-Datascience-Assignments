 # 2.Write a program to check whether an element exists in a tuple or not.

t = (10, 20, 30, 40, 50)

element = int(input("Enter element: "))

if element in t:
    print("Element exists")
else:
    print("Element does not exist")
