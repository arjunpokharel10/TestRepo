# Write a Python program that:
# ● Takes a string as input.
# ● Reverses the string.
# ● Counts the number of vowels (a, e, i, o, u) in the string.
# ● Converts the string to uppercase.


def vowel_counter():
    string = input("enter a word or a phrase:")
    vowel = "aeiou"
#    counter = sum(1 for char in string if char in vowel)  # another way to do, which replaces the 4 lines below
    counter = 0
    for i in string:
        if i in vowel:
            counter += 1

    print(f">>{string}<< has {counter} vowels")



vowel_counter()
