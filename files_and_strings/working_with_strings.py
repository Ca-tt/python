books_to_read = [
  'The Suble Art of Not Giving a Fuck',
  '48 Laws of Power',
  'Lucky Starr'
]

# Loop through array of strings
print('Books I\'d like to read in 3 months:')
for book in books_to_read:
  print('-', book)

# Find string length
word = 'banana'
index = 0
count = 0

# Solution
while index < len(word):
  print(index, word[index], count)
  index += 1
  count = index + 1

# More elegant solution
for letter in word:
  count += 1
  print(letter, count)