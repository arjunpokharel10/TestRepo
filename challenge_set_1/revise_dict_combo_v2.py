# Write a Python function that:
# ● Takes a string as input.
# ● Counts the frequency of each character in the string and stores it in a dictionary.
# ● Ignores spaces and considers case-insensitive comparisons.

def character_frequency_count(string_to_evaluate):
    character_count = {}
    for char in string_to_evaluate.replace(' ',''):
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    return character_count


string_inserted = input("enter a string: ")
result = character_frequency_count(string_inserted)

print(result)
