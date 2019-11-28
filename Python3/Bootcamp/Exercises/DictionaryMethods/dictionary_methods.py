inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
print(f'{inventory =}')

stock_list = inventory.copy()
print(f'{stock_list =}')

stock_list['hot cheetos'] = 25
stock_list.update({'cookie' : 18})

stock_list.pop('cake')
print(f'{stock_list =}')