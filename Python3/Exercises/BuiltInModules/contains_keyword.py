from keyword import iskeyword

def contains_keyword(*arg):
    for string in arg:
        if iskeyword(string):
            return True
    return False

print(contains_keyword("hello", "goodbye"))