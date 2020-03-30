def copy_and_reverse(file1, file2):
    with open(file1) as file:
        data = file.read()
    
    with open(file2, 'w') as file:
        file.write(data[::-1])