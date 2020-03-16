def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)
    
num = (1, 2, 3, 4, 5, 6)
sum_all_values(*num)