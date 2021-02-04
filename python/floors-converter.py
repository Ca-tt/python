# type floor and country
floor = int(input('Please, enter the floor: '))
region = input('Please choose the region you\'re in (EU/US): ')

# check the region
if region == 'EU':
  floor = floor - 1

# print the answer
print('You\'re on the floor:', floor)