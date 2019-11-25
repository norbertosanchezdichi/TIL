list1 = [range(1, 5)]
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