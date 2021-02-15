data = 'Sent from damir96.lukyanenko@gmail.com at Feb 2 09:16:22 2021'

at_sign_position = data.find('@')
print(at_sign_position)

email_end_position = data.find(' ', at_sign_position)
print(email_end_position)

email_adress = data[at_sign_position: email_end_position]
print(email_adress)
