import re

def is_valid_time(input):
    time_regex = re.compile(r'^\d\d?:\d\d$')
    if time_regex.search(input):
        return True
    return False
    
print(is_valid_time("10:45"))       #True
print(is_valid_time("1:23"))        #True
print(is_valid_time("10.45"))       #False
print(is_valid_time("1999"))        #False
print(is_valid_time("145:23"))

print(is_valid_time("it is 12:15")) #False
print(is_valid_time("12:15"))      #True