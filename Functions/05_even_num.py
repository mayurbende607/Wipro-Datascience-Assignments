# 5.Write a function to print the even numbers from a given list. List is passed to the function as an argument.
   

def even_numbers(lst):
    result = []

    for num in lst:
        if num % 2 == 0:
            result.append(num)

    print(result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers(numbers)
