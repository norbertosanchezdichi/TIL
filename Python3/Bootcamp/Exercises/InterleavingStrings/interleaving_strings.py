def interleave(string1, string2):
    string1_expand = [char for char in string1]
    string2_expand = [char for char in string2]
    return zip(string1_expand, string2_expand)
    
print(interleave('hi', 'ha'))