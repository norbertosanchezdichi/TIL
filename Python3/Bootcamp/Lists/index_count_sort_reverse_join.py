numbers = [3, 5, 1, 1, 7, 10, 3]
print(numbers)

print(f'Index of 5 is {numbers.index(5)}')
print(f'Index of second 1 is {numbers.index(1, 3)}')
print(f'Index of last 3 is {numbers.index(3, len(numbers) - 3, len(numbers) - 1)}')