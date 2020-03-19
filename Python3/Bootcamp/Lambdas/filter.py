listOfNums = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, listOfNums))
print(listOfNums)
print(evens)

names = ['austin', 'penny', 'anthony', 'angel', 'billy']
a_names = list(filter(lambda n: n[0]=='a', names))
print(names)
print(a_names)

names = ['Lassie', 'Norberto', 'Rusty']

print(names)
print(list(map(lambda name: f"Your instructor is {name}", filter(lambda v: len(v) > 6, names))))
print([f'Your instructor is {name}' for name in names if len(name) > 6])