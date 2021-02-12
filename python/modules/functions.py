import sys
sys.path.append('../')

# Split file into words
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

# Make a value-key array (e.x for a future sorting) 
def create_value_key_array(array):
  value_key_array = []

  for key, value in array.items():
    # print('key', key, '\t', 'value', value)
    value_key_array.append((value, key))

  return value_key_array
#===

# Sort array by keys in a reverse order
def sort_array_reverse(array):
  array = sorted(array, reverse=True)
  return array
