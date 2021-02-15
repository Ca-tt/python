numbers = [
    1,
    3,
    11,
    24,
    75,
    105,
    202,
    303
]

find = 105


def binary_search(array, find):
  cycles = 0

  low = 0
  high = len(array) - 1

  while low <= high:
    print(
        'low:', low,
        'high', high)

    mid = int((low + high) / 2)
    print('mid', mid)

    guess = array[mid]

    if find < guess:
      print('find is less than mid')
      high = mid + 1
      print(
          'new high is', high,
          'low is', low
      )

    elif find > guess:
      print('find is greater than mid')
      low = mid + 1
      print(
          'new low is', low,
          'high is', high
      )

    elif guess == find:
      print('we found', mid)
      break

    cycles = cycles + 1
    print('cycle', cycles)


binary_search(numbers, find)
