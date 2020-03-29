def yes_or_no():
    count = 2
    while True:
        if count % 2:
            yield 'no'
        else:
            yield 'yes'
        count += 1
            
gen = yes_or_no()
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) # 'yes'
print(next(gen)) # 'no'