import pdb

first = "First"
second = "Second"
result = first + second
#pdb.set_trace()
third = "Third"
result += third
print(result)

def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace()
    
    return a + b + c + d

# Also used in one line
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# c (exist)
# p (print)