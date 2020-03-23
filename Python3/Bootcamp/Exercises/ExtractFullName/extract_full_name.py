def extract_full_name(listOfNames):
    return [name['first'] + ' ' + name['last'] for name in listOfNames] 
    
print(extract_full_name([{'first': 'Norberto', 'last': 'Sánchez-Dichi'}, {'first': 'Ace', 'last': 'Ventura'}]))