# File url
url = 'txt/mbox-short.txt'

# Find the file name and print it out
last_slash_pos = url.rindex('/') + 1

filename = url[last_slash_pos:]
print('File name:', filename)

# Open the file
try:
  file = open(url, 'r')
except:
  print('No such file or directory. Plese check the path to the file')
  quit()

data = file.read()
file.seek(0)
# print(len(data))

# Count file lines
lines = 0
for line in file:
  lines += 1
print('File lines:', lines)

# Return cursor to the file beginning
file.seek(0)

# Count how much mail we receivede
received_emails = 0

for line in file:
  if line.startswith('From:'):
    received_emails += 1
    print(line.rsplit())

print('received_emails:', received_emails)
