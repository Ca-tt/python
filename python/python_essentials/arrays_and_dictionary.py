# To-do
# find unique names
# and count them
# into dictionary
# name[unique_name] = unique_name

set_of_names = [
    'Net', 'Seth', 'Lapis', 'Anubis', 'Maat', 'Nour', 'Rashida', 'Adom', 'Seth', 'Lapis', 'Nour', 'Rashida', 'Adom', 'Nour', 'Rashida', 'Adom', 'Seth', 'Net', 'Seth', 'Lapis', 'Anubis', 'Maat', 'Net', 'Seth', 'Lapis', 'Anubis', 'Maat'
]

names = {}

# Solution
for name in set_of_names:
  if name not in names:
    names[name] = 1
    print(names)
  else:
    names[name] = names[name] + 1

print(names)

# To-do:
# Create a digital crypto wallet

account = {}

assets = [
    ['bitcoin', 1.25],
    ['ripple', 56],
    ['ethereum', 2.2],
    ['bitcoin', 1.25],
    ['ripple', 56],
    ['bitcoin', 1.25],
    ['ripple', 56],
    ['ethereum', 2.5]
]

# Solution
for asset in assets:
  if asset[0] not in account:
    account[asset[0]] = asset[1]
    print(asset)
  else:
    account[asset[0]] += asset[1]
print('account:', account)

print('bitcoin value in account:', account.get('bitcoin'))

# Advanced solution
for asset in assets:
  account[asset[0]] = account.get(asset[0], 0) + asset[1]
print('account:', account)

