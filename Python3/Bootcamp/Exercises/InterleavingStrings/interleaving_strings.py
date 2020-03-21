def interleave(string1, string2):
    string1_expand = [char for char in string1]
    string2_expand = [char for char in string2]
    string1string2 = list(zip(string1_expand, string2_expand))
    string_a = [c[0] + c[1] for c in string1string2]
    
    string = ''
    for string_b in string_a:
        string += string_b
        
    return string
    
print(interleave('hi', 'ha'))