#List of Numbers
more_numbers = [6, 1, 8, 2]
print(f'more_numbers = {more_numbers}')
print(f'sorted more_numbers = {sorted(more_numbers)}')
print(f'sorted more_numbers in reverse = {sorted(more_numbers, reverse = True)}')

#Dictionary

users = [
    {"username": "samuel", "tweets": ["I love cake", "i love fruit"]},
    {"username": "katie", "tweets": ["I love my cate"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []},
]

print(f'users = {users}')
print(f'sorted users by length = {sorted(users, key=len)}')
print(f'sorted users by alphabetical order = {sorted(users, key=lambda user: user["username"])}')
print(f'sorted users by alphabetical order = {sorted(users, key=lambda user: len(user["tweets"]), reverse = True)}')