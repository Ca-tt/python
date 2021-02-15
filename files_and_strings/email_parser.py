import re

# * Task description
# * Parse email lists. Extract useful information
# * Save information into associative array:
# * mail -> username, date, SPAM level etc

# //// TODO 1) Extract user emails
# //// TODO 2) Extract usernames
# //// TODO 3) Extract full dates (time and date)
# //// TODO 4) Extract SPAM-Confidence
# //// TODO 6) Save data accordingly
# TODO 7) Sort saved data
# TODO 8) Print the result

# Desired outcome
desired_array = {
    'email': ['username', 'date', 'spam-confidence']
}


# * Solution

# //TODO add try-catch for a file opening
file = open('modules/txt/mbox-short.txt')

user_db = {}


# when stop_signal is reached, save data to new key
# * Stop Flag

email_pattern = 'From: (\S+@\S+)'
username_patten = 'From: (\S+)@'
date_pattern = 'Date: (\d.+) -0500'
spam_pattern = 'X-DSPAM-Confidence: (.+)'

# * Stop signal
stop_pattern = 'This automatic notification.'

# for line in file:
#   email += re.findall(email_pattern, line)
#   date += re.findall(date_pattern, line)
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

for user, data in user_db.items():
  print(user, data)

# print(user_db)

  # # print(date)
  # if email:
  #   # Separate username from email
  #   username = email[0].split('@')[0]
  #   user_db[email[0]] = [username, index]
  # if date:
  #   print(date, username)
  #   # user_db[username] = date
