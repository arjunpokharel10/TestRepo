# Write a Python function that:
# ● Accepts a list of integers as input. (use split method)
# ● Returns the largest and smallest number in the list.
# ● Removes duplicates from the list.
# ● Sorts the list in descending order.

def remove_duplicates_and_sort_given_numbers():
    x = input("enter some numeric values in digits, separated by space: ")
    x = list(set(map(int, x.replace(',',' ').split())))
    x.sort()
    print(f"the input in sorted order, and without duplicates, is: {x}\nthe smallest is {x[0]} and the largest is {x[-1]}")

remove_duplicates_and_sort_given_numbers()