#Using list comprehension
def extract_full_name(listOfNames):
    return [name['first'] + ' ' + name['last'] for name in listOfNames] 
    
#Using map(..)
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

print(extract_full_name([{'first': 'Norberto', 'last': 'Sánchez-Dichi'}, {'first': 'Ace', 'last': 'Ventura'}]))