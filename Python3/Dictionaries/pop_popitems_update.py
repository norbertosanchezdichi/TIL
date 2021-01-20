student = {
    'name': 'Norberto',
    'owns_parrot' : True,
    'favorite_language': 'Python',
    25 : 'my favorite number!'}
print(f'{student =}')

print(f'{student.pop(25) =}')
print(f'{student =}')

print(f'{student.popitem() =}')
print(f'{student.popitem() =}')
print(f'{student =}')

person = {'city': 'Los Angeles'}
print(f'{person =}')
person.update(student)
print(f'{person =}')
person['name'] = 'Otrebron'
print(f'{person =}')
person.update({})
print(f'{person =}')