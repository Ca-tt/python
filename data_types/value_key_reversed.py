unsorted_data = {
    'christmas tree': 11,
    'garland': 17,
    'toy': 43,
    'red star': 14,
    'blue star': 14,
}

# To do
# sort data by value, not key


def value_key_array(array):
  value_key_array = []

  for key, value in array.items():
    value_key_array.append((value, key))

  return value_key_array
#===


sorted_array = value_key_array(unsorted_data)
print('value-key array:', sorted_array)


def sort_array(array):
  array = sorted(array, reverse=True)
  return array


result = sort_array(sorted_array)
print('reverse-sorted array:', result)
