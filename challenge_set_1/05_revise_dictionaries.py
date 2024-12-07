# Write a Python program that:
# ● Creates a dictionary with keys as numbers from 1 to 5 and values as their squares.
# ● Prints all the keys and values.
# ● Updates the value of key 3 to 27.
# ● Deletes the key 5 from the dictionary.


def keys_as_numbers_values_as_squares():
    init_num_squared = {}
    for i in range (1, 6):
        x = i**2
        init_num_squared[i] = x
    return init_num_squared

result_pairs = keys_as_numbers_values_as_squares()
print(result_pairs)

result_pairs[3] = 27
print(result_pairs)

result_pairs.pop(5)
print(result_pairs)

dat_type = result_pairs.keys()
print(dat_type)
print(type(dat_type))

items_dict = set(result_pairs.items())
print(items_dict)
print(type(items_dict))


