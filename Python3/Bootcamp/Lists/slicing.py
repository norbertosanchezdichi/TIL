# Using start parameter

list1 = list(range(1, 5))
print(list1)

list2 = list1[1:]
print(list2)

list3 = list1[3:]
print(list3)

list4 = list1[-1:]
print(list4)

list5 = list1[-3:]
print(list5)

list6 = list1[:]
print(list6)
print(f'list6 is list1 : {list6 is list1}')
print(f'list6 == list1: {list6 == list1}')

# Using end parameter

list7 = list1[:2]
print(list7)

list8 = list1[2:4]
print(list8)

list9 = list1[1:-1]
print(list9)