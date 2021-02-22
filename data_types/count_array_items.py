# TODO: count unique names and
# write them into dictionary

# Given array to count
names_array = [
    'Net', 'Seth', 'Lapis', 'Anubis', 'Maat', 'Nour',
    'Rashida', 'Adom', 'Seth', 'Lapis', 'Nour', 'Rashida',
    'Adom', 'Nour', 'Rashida', 'Adom', 'Seth', 'Net',
    'Seth', 'Lapis', 'Anubis', 'Maat', 'Net', 'Seth',
    'Lapis', 'Anubis', 'Maat'
]

# Solution
def count_array_elements(array):
    new_dict = {}

    for name in array:
        new_dict[name] = new_dict.get(name, 0) + 1
    return new_dict

# Print the solution
print(count_array_elements(names_array))
