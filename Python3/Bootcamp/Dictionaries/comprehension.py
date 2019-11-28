numbers = dict(first = 1, second = 2, third = 3)

print(f'{numbers =}')
print(f"{ {key:value ** 2 for key, value in numbers.items()} =}")

print(f"{ {num: num ** 2 for num in list(range(1,6))} }")