cities = {'Los Angeles', 'San Jose', 'San Luis Obispo', 'Los Angeles'}

print(f'{cities =}')

cities.add('San Diego')
print(f'{cities =}')

cities.remove('Los Angeles')
print(f'{cities =}')

cities.discard('Santa Clara')

print(f'{cities.copy() =}')
print(f'{cities.copy() is cities =}')

