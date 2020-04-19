import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')

res = pattern.search("r5435r325r234 jkl;")
print(res)

res = pattern.search("call me at 310 445-9876")
print(res.group())

res = pattern.findall("call me at 310 445-9876 432 432-5433")
print(res)

res = re.search(r'\d{3} \d{3}-\d{4}', "call me at 310 445-9876").group(
print(res)