import re

# * TODO: Parse an email list, save user info into a dictionary.

def open_file(filename):
  """Returns a stream to a file"""
  try:
    file = open(filename, 'r')
  except:
    print('No such file or directory. Plese check the path to the file')
    quit()
  return file

# Regexp for info extracting
email_pattern = 'From: (\S+@\S+)'
username_patten = 'From: (\S+)@'
date_pattern = 'Date: (\d.+) -0500'
spam_pattern = 'X-DSPAM-Confidence: (.+)'
# Stop pattern
stop_pattern = 'This automatic notification.'


def info_extracting(file):
  user_db = {}
  current_index = 1

  for line in file:
    # Boolean
    new_user_flag = re.search(stop_pattern, line)

    while(current_index):
      # print('Extracting data for user #', current_index, '...', '\n')

      email = re.findall(email_pattern, line)
      date = re.findall(date_pattern, line)
      spam_confidence = re.findall(spam_pattern, line)

      if email:
        # Separate username from email
        username = email[0].split('@')[0]
        # user_db[email[0]] = [username, current_index]
        user_db[current_index] = [email[0], username]

      if date:
        # print(date, username)
        user_db[current_index] += date

      if spam_confidence:
        # print(spam_confidence[0])
        user_db[current_index] += spam_confidence

      if new_user_flag:
        # print(line.rstrip())
        # print('End operation...')
        current_index += 1

      break
  return user_db

# Opening file
file = open_file('../txt/mbox-short.txt')

# Extracting the info
result = info_extracting(file)

# Printing the result
for user, data in result.items():
  print(user, data)