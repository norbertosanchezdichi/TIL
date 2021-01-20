numbers = list(range(1,4))
print(numbers)
print(f'{[x * 10 for x in numbers] =}') 

name = 'norberto'
print(name)
print(f'{"".join([letter.upper() for letter in name]) =}')

list1 = [0, '', False]
print(f'{list1 =}')
print(f'{[bool(value) for value in list1] = }')