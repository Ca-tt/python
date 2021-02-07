numbers = [3, 33, 12, 35, 67, 98, 756, 434, 55, 666]
largest_number = -9999

print('the largest number is:', largest_number)

# Find largest number
for el in numbers:
  if el > largest_number:
    largest_number = el
    print('the NEW largest number is:', largest_number)

numbers = [10, 22, -23, -1, 0, 55, -3, -6, 9]
negative_sum = 0

print('negative_sum is:', negative_sum)

# Find smallest number
for el in numbers:
  if el < 0:
    negative_sum -= el
    print('negative_sum is:', negative_sum)
