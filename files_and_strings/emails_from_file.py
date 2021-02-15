file = open('txt/mbox-short.txt')

for line in file:
  if not line.startswith('From '):
    continue
  # clear the line
  line = line.rstrip()
  # split into words
  words = line.split()
  # find email word position
  email = words[1]
  # print(email)

  user_data = email.split('@')
  private_info = user_data[0]
  email_host = user_data[1]
  print('private_info:', private_info)
  print('email_host:', email_host)
