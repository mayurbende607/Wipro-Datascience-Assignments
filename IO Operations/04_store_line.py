# 4.Write a program to read contents from a txt file line by line and store each line into a list.

file = open("sample.txt", "r")

lines = file.readlines()

file.close()

print(lines)
