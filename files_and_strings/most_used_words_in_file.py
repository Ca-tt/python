import sys
sys.path.append('../')

from python.modules.functions import (
  split_file_into_words,
  create_value_key_array, 
  sort_array_reverse,
  print_array_key_value
)
# To do
# find 10 most common words in filename

# stages
# 1) read the file
# 2) count words
# 3) choose 10 most common words


splitted_text = split_file_into_words('txt/mbox-short.txt')
# print(splitted_text)

tuppled_array = create_value_key_array(splitted_text)
# print(tuppled_array)

sorted_array = sort_array_reverse(tuppled_array)
# print(sorted_array)

print_array_key_value(sorted_array[:10])

