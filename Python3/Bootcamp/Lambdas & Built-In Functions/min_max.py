print(f'{max(3, 67 ,9)}')
print(f'{max("awesome")}')
print(f'{max({1:'a', 3:'c', 2:'b'})}')

print(f'{min(3, 67 ,9)}')
print(f'{min("awesome")}')
print(f'{min({1:'a', 3:'c', 2:'b'})}')

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(f'{min(len(name) for name in names)}')
print(f'{min(names, key=lambda n:len(n))}')

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(f'{min(songs, key=lambda s: s['playcount'])}')
print(f'{max(songs, key=lambda s: s['playcount'])['title']}')