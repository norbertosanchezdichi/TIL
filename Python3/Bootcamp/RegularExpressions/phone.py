import re

def extra_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

print(extract_phone("my number is 323 240-4325"))
print(extract_phone("my number is 323 240-43224"))
print(extract_phone("323 240-4322"))

def extra_all_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.find_all(input)
    
print(extract_all_phone("my number is 323 240-4325 or call me here 423 432-4321"))
print(extract_all_phone("my number is 323 240-43224"))

#def is_valid_phone():