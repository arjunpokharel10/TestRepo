# Write a Python function that:
# ● Takes a tuple of integers as input.
# ● Returns a new tuple with only the even numbers from the original tuple.
# ● Converts the tuple into a list and adds a new element to it.

def convert_digits_to_tuple():
    digits_as_sting = input("enter some digits (numeric values): ")
    digits_to_tuple = tuple(map(int, digits_as_sting.replace(',','').split()))
    return digits_to_tuple

def main_show_even_numbers():
    ints_to_analyse = convert_digits_to_tuple()
    even_numbers = []
    for i in ints_to_analyse:
        if i % 2 == 0:
            even_numbers.append(i)
    even_numbers = tuple(even_numbers)
    return even_numbers

    

evens = main_show_even_numbers()
print(evens)

evens = list(evens)
evens.append(101)
print(evens)
