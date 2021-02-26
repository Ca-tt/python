import sys
sys.path.append('../')
# To do
# find 10 most common words in filename

# stages
# 1) read the file
# 2) count words
# 3) choose 10 most common words

import sys
sys.path.append('../')

# * Split file into words
def split_file_into_words(filename):

  url = filename
  words_array = {}
  file = None

  try:
    file = open(filename)
  except:
    print(
      'There\'s no file at', url,
      '\n', 'Please, check the file\'s address'
    )

  for line in file:
    words = line.split()

    for word in words:
      # write words as keys to new array
      # provide the initial value (1) for new keys
      words_array[word] = words_array.get(word, 0) + 1

  return words_array
#===

# * Make a value-key array (e.x for a future sorting)
def create_value_key_array(array):
  value_key_array = []

  for key, value in array.items():
    # print('key', key, '\t', 'value', value)
    value_key_array.append((value, key))

  return value_key_array
#===

# * Sort array by keys in a reverse order
def sort_array_reverse(array):
  array = sorted(array, reverse=True)
  return array

# * Print key-values of array
def print_array_key_value(array):
  for key, value in array:
    print(key, '\t', value)


splitted_text = split_file_into_words('../txt/mbox-short.txt')
# print(splitted_text)

tuppled_array = create_value_key_array(splitted_text)
# print(tuppled_array)

sorted_array = sort_array_reverse(tuppled_array)
# print(sorted_array)

print_array_key_value(sorted_array[:10])

