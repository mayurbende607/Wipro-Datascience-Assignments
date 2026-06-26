# 6.Write a program to sum all the values in a dictionary, considering the values will be of int type.

dic = {1: 10,2: 20,3: 30,4: 40}

total = 0

for value in dic.values():
    total = total + value

print("Sum =", total)
