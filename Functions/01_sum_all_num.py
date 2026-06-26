 # 1.Write a function to return the sum of all numbers in a list.

def sum_list(lst):
    total = 0

    for num in lst:
        total += num

    return total


numbers = [8, 2, 3, 0, 7]

print("Sum =", sum_list(numbers))
