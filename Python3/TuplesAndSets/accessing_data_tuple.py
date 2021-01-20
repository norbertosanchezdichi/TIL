first_tuple = (1, 2, 3, 3, 3)
print(f'{first_tuple =}')

print(f'{first_tuple[1] =}')
print(f'{first_tuple[-1] =}')
print(f'{first_tuple.index(1) =}')

locations = {
    (35.6895, 39.6917): "Tokyo Office"
}
print(f'{locations =}')
print(f"{locations[(35.6895, 39.6917)] =}")
print(f"{locations.items() =}")