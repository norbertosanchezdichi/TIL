nested_list = [range(1,4), range(4,7), range(8,10)]
print(f'{nested_list =}')
print(f'{[[single_list for single_list in nested_list] for number in nested_list]}')