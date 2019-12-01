numbers = dict(first = 1, second = 2, third = 3)

print(f'{numbers =}')
print(f"{ {key:value ** 2 for key, value in numbers.items()} =}")

print(f"{ {num: num ** 2 for num in list(range(1,6))} =}")

string1 = 'ABC'
print(f"{string1 =}")
string2 = '123'
print(f"{string2 =}")
print(f"{ {string1[i]: string2[i] for i in range(0, len(string1))} =}")

print(f"{ {num: ('even' if num % 2 == 0 else 'odd') for num in numbers.values()} =}")