def get_unlimited_multiples(num = 1):
    next_num = num
    while True:
        yield next_num
        next_num += num
        
two = get_unlimited_multiples(7)
print(next(two))
print(next(two))
print(next(two))
print(next(two))
print(next(two))
print(next(two))