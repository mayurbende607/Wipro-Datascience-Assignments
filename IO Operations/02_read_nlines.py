# 2.Write a program to read first n lines from a txt file. Get n as user input.

n = int(input("Enter number of lines: "))

file = open("sample.txt", "r")

for i in range(n):
    print(file.readline(), end="")

file.close()
