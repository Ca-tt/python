# Arrays
# 1) All data stored contiguously (right next to each other) in memory

# Pros:
# - better at Reading
# - - can instantly acess any cell (item) array[item]
# - better at Random Accesing

# Cons:
# - bad at any types of moving memory (instert, delete)
# - - have to store all cells at once

usernames = [
    'cracking',
    'larry',
    'james16',
    'dwentydwenty',
    'jimmy1826',
    'xDannyCoachx',
]

# Linked Lists
# 1) With linked lists, your items can be anywhere in memory.
# 2) Each item stores the address of the next item in the list
# 3) With linked lists, you never have to move your items.
# 4) Linked lists are great if you’re going to read all the items one at a time

# Pros:
# - better at Inserts
# - better at Deletes

# Cons:
# - can't jump around (random acess) the cells (items)
# - sequential acess

user_data = {
    'cracking': 'cracking@gmail.com',
    'larry': 'larry@gmail.com',
    'james16': 'james16@gmail.com',
    'dwentydwenty': 'dwentydwenty@gmail.com',
    'jimmy1826': 'jimmy1826@gmail.com',
    'xDannyCoachx': 'xDannyCoachx@gmail.com',
}
