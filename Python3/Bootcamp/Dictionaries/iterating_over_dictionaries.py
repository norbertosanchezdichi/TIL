student = {
    'name': 'Norberto',
    'owns_parrot' : True,
    'favorite_language': 'Python',
    25 : 'my favorite number!'}

print(f'{student.values() =}')
for value in student.values():
    print(value)

print(f'{student.keys() =}')
for key in student.keys():
    print(key)
    
print(f'{student.items() =}')
for key, value in student.items():
    print(key, value)

