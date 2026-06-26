 # 5.Write a program to replace last value of tuples in a list to 100.

lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

new_list = []

for t in lst:
    new_tuple = t[:-1] + (100,)
    new_list.append(new_tuple)

print(new_list)
