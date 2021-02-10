numbers = [
    1,
    4,
    10,
    11,
    25,
    36,
    78,
    33,
    44,
    83,
    121,
    9
]

low = 0
high = max(numbers)

find = 11
mid = 0

cycles = 0

print('low:', low, 'high', high)


while low <= high:

  mid = int((low + high) / 2)
  print('mid', mid)

  if find < mid:
    print('find is less than mid')
    high = mid + 1
    print(
        'new high is', high,
        'low is', low
    )

  elif find > mid:
    print('find is greater than mid')
    low = mid + 1
    print(
        'new low is', low,
        'high is', high
    )

  elif mid == find:
    print('we found', mid)
    break

  cycles = cycles + 1
  print('cycle', cycles)
