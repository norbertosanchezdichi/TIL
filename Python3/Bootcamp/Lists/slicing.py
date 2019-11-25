print('Using start parameter')

list1 = list(range(1, 5))
print(f'list1 = {list1}')

list2 = list1[1:]
print(f'list1[1:] = {list2}')

list3 = list1[3:]
print(f'list1[3:] = {list3}')

list4 = list1[-1:]
print(f'list1[-1:] = {list4}')

list5 = list1[-3:]
print(f'list1[-3:] = {list5}')

list6 = list1[:]
print(f'list6 = {list6}')
print(f'list6 is list1 : {list6 is list1}')
print(f'list6 == list1: {list6 == list1}')

print('\nUsing end parameter')

list7 = list1[:2]
print(f'list1[:2] = {list7}')

list8 = list1[2:4]
print(f'list1[2:4] = {list8}')

list9 = list1[1:-1]
print(f'list1[1:-1] = {list9}')

print('\nUsing step parameter')

list10 = list1[1::2]
print(f'list1[1::2] = {list10}')

list11 = list1[::3]
print(f'list1[::3] = {list11}')

list12 = list1[1::-1]
print(f'list1[1::-1] = {list12}')

print('\nTricks with slicing')

string = "This is fun!"
print(f'string = {string}')
print(f'string[::-1] = {string[::-1]}')

list1[2:3] = ['he', 'he']
print(f'list[2:3] = [\'he\', \'he\'] results in {list1}')