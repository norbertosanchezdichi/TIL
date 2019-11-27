artist = {
    "first": "Neil",
    "last": "Young",
}

print(f'{artist =}')

print('Concatenation Solution')
print(f'{artist["first"] + " " + artist["last"] =}')

print('Format() Solution')
print(f'{"{{}} {{}}".format(artist["first"], artist["last"] =}')

print('f-String Solution')
print(f'{artist["first"]} {artist["last"] =}')