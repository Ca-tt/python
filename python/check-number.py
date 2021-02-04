user_age = input('Please, type your age: ')
try:
  result_age = int(user_age)
except: 
  result_age = 'Error'

print('The user\'s age is:', result_age)

