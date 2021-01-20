def copy(file1, file2):
    with open(file1) as file:
        data = file.read()
    
    with open(file2, 'w') as file:
        file.write(data) 
        
copy('story.txt', 'copy of story.txt')