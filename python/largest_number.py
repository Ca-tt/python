numbers = [3, 33, 12, 35, 67, 98, 756, 434, 55, 666]
largest_number = -9999

print('the largest number is:', largest_number)

for el in numbers:
  if el > largest_number:
    largest_number = el
    print('the NEW largest number is:', largest_number)
