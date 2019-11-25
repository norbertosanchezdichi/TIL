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
print(list6)
print(f'list6 is list1 : {list6 is list1}')
print(f'list6 == list1: {list6 == list1}')

print('Using end parameter')

list7 = list1[:2]
print(f'list1[:2] = {list7}')

list8 = list1[2:4]
print(f'list1[2:4] = {list8}')

list9 = list1[1:-1]
print(f'list1[1:-1] = {list9}')