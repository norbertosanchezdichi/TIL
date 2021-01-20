def is_all_strings(iterable):
    return all(isinstance(string, str) for string in iterable)
    
print(['a', 'b', 'c'])
print([2, 'a', 'b', 'c'])