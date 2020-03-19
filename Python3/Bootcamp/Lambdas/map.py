nums = [1, 2, 3, 4]
doubles = map(lambda x: x*2,nums)

print(f'{doubles.__name__}')
print(f'{list(doubles)}')
print(f'{list(doubles)}')

doubles = list(map(lambda x: x*2))
print(f'{doubles}')

evens = list(map(lambda x: x*2, nums))
print(f'{evens}')