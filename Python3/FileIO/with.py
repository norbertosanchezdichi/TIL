with open("story.txt") as file:
    data = file.read()
    
print(file.closed)
print(data)