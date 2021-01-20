def sum_even_values(*args):
    return sum(args for args in args if args % 2 == 0)
    
print(sum_even_values(1, 2, 3, 4, 5, 6))