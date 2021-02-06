# write the program which shows greetings based on choosen language
# languages are: ru, en, fr
# user have to write of these options. Other're forbidden

# ask user to choose the language
greeting = None
userLanguage = input('What\'s your language? (ru/en/fr): ')

# check the correctness of user's input
if userLanguage == 'ru' or userLanguage == 'en' or userLanguage == 'fr':
  greeting = userLanguage
else:
  userLanguage = input('Please, pick up one of three options: (ru/en/fr) ')
  greeting = userLanguage

# pick the right greeting based on user's language


def greet(userLanguage):
  if userLanguage == 'ru':
    greeting = 'Privet!'
    return greeting
  elif userLanguage == 'en':
    greeting = 'Hello'
    return greeting
  elif userLanguage == 'fr':
    greeting = 'Bonjour'
    return greeting


# print the greeting
print(greet(userLanguage))


# Better solution of the problem. But not the best
while True:
  entry = input('What\'s your language? (ru/en/fr): ')
  if entry == 'ru':
    print('Privet!')
    break
  elif entry == 'en':
    print('Hello')
    break
  elif entry == 'fr':
    print('Bonjour')
    break
  else:
    entry = input('Please, pick up one of three options: (ru/en/fr) ')