student = {
    'name': 'Norberto',
    'owns_parrot' : True,
    'favorite_language': 'Python',
    25 : 'my favorite number!'}

print(f'{student = }')

student_copy = student.copy()
print(f'{student_copy = }')

student_copy.clear()
print(f'{student_copy = }')

new_student = {}.fromkeys(student.keys(), None)
print(f"{new_student = }")
print(f"{new_student.get('name')}")