import re

def extra_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.search(input)
    return match.group()
    
print(extract_phone("my number is 323 240-4325"))
print(extract_phone("my number is 323 240-43224"))

#def is_valid_phone():