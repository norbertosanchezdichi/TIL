nested_list = [list(range(1,4)), list(range(4,7)), list(range(8,10))]
print(f'{nested_list =}')
print(f'{[[single_list for single_list in nested_list] for single_list in nested_list] =}')

print(f'{[["X" if num % 2 == 0 else "O" for num in range(1,4)] for num in range(1,4)] =}')