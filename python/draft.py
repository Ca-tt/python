import sys
sys.path.append('../')

# To do
# find 10 most common words in filename

# stages 
# 1) read the file
# 2) count words
# 3) choose 10 most common words 


from python.module.methods import * 


splitted_text = split_file_into_words('txt/mbox-short.txt')
# print(splitted_text)

tuppled_array = create_value_key_array(splitted_text)
# print(tuppled_array)

sorted_array = sort_array_reverse(tuppled_array)
# print(sorted_array)

print(sorted_array[:10])

