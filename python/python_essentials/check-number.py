user_age = input('Please, type your age: ')
result_age = None

try:
  result_age = int(user_age)
except: 
  result_age = 'Error'

print('The user\'s age is:', result_age)

