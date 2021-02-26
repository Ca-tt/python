numbers = [
    1, 4, 10, 11, 25, 36,
    78, 33, 44, 83, 121, 9
]

to_find = 11

def binary_search(number):

    cycles = 0

    low = 0
    high = max(numbers)

    print('low:', low, 'high', high)

    while low <= high:

      mid = int((low + high) / 2)
      print('mid', mid)

      if number < mid:
        high = mid + 1
        print('number is less than mid')
        print(
            'new high is', high,
            'low is', low
        )

      elif number > mid:
        low = mid + 1
        print('number is greater than mid')
        print(
            'new low is', low,
            'high is', high
        )

      elif mid == number:
        print('we found', mid)
        break

      cycles = cycles + 1
      print('cycle', cycles)

binary_search(to_find)