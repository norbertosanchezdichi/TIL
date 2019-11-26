numbers = list(range(1, 7))
print(numbers)
print(f'{[number for number in numbers if number % 2 == 0] =}')
print(f'{[number for number in numbers if number % 2 != 0] =}')
print(f'{[number * 2 if number % 2 == 0 else number / 2 for number in numbers] =}')

with_vowels = 'This is so much fun!'
vowels = 'aeiou'
print(f'{"".join(char in for char in with_vowels if char not in vowels) =}')