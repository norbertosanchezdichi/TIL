file = open("story.txt")

print(file.read())
print(file.seek(0))
print(file.read())

print(file.seek(0))
print(file.readline())
print(file.readline())

print(file.seek(0))
print(file.readlines())

print(file.closed)
print(file.close())
print(file.closed)