# 3.Write a program to accept input from user and append it to a txt file.

text = input("Enter text: ")

file = open("sample.txt", "a")

file.write(text + "\n")

file.close()

print("Data appended successfully.")
