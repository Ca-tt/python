# Task
# Count the most and less used words
# in a set of words
# use lorem.txt as words source

url = '../txt/lorem.txt'
try:
  file = open(url, 'r')
except:
  print('No such file or directory. Plese check the path to the file')
  quit()

file_data = file.read()
file.seek(0)

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
