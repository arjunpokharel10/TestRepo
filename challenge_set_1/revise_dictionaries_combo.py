# Write a Python function that:
# ● Takes a string as input.
# ● Counts the frequency of each character in the string and stores it in a dictionary.
# ● Ignores spaces and considers case-insensitive comparisons.


'''
 feedback from the teacher: this is unnecessarily convoluted and inelegant. 
 for example, sorted() function is expensive. using set() function to weed out duplicates is unnecessary for the solution
 unnecessary nested if function
 
 re-factored solution in revies_dict_combo_v2.py

'''

def takes_strings_as_input():
    strings_taken = input("enter your words or phrases: ").lower()
    return strings_taken

def counts_chars_in_string():
    string_to_evaluate = takes_strings_as_input()
    distinct_chars_in_the_string = sorted(list(set(string_to_evaluate.replace(' ',''))))

    frequency_counter = {}
    for key in distinct_chars_in_the_string:
        key_freq = 0
        for vals in string_to_evaluate:
            if vals == key:
                key_freq += 1
        frequency_counter[key] = key_freq

    return frequency_counter


result = counts_chars_in_string()
print(result)
print(type(result))  



