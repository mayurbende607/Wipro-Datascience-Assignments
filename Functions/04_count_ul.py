# 4.Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

def count_letters(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)


text = input("Enter a string: ")

count_letters(text)
