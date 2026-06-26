# 6.Write a program to count the frequency of a user entered word in a txt file.

word = input("Enter word to search: ")

file = open("sample.txt", "r")

text = file.read()

file.close()

words = text.split()

count = words.count(word)

print("Frequency =", count)
