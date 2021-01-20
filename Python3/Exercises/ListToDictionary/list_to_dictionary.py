person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
print(f'{person =}')

print('Using Dictionary Comprehension')
print(f"{ {person[i][0]: person[i][1] for i in range(0, len(person))} =}")

print('Using Dictionary Comprehension Without References to List Indexes')
print(f"{ {keys:values for keys,values in person} =}")

print('Using dict(..)')
print(f"{dict(person) =}")