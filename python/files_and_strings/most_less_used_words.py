# Task
# Count the most and less used words
# in a set of words
# use lorem.txt as words source

url = 'txt/lorem.txt'
file = open(url)

file_data = file.read()
file.seek(0)

# Simple solution
# ===

words = file_data.split()

result = {}
for word in words:
  result[word] = result.get(word, 0) + 1

# ===
numbers = []

max_count = 0
min_count = 10

max_word = None
min_word = None

for key in result:
  if result[key] > max_count:
    max_count = result[key]
    max_word = key
    # print('max', max_word, max_count)
    
  elif result[key] < min_count:
    min_count = result[key]
    min_word = key
    # print('min', min_word, min_count)

# print(result)

# Advanced solution
# ===
data = {}
max_number = 0
max_word = 0

for line in file:
  # split lines into words
  words = line.split()
  for word in words:
    # count values for keys
    data[word] = data.get(word, 0) + 1
    for key, value in data.items():
      # find the greatest repetition of the key
      if value > max_number:
        max_number = value
        max_word = key


print(max_word, max_number)
