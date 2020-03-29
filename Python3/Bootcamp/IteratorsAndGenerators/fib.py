def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums
    
def fib_gen(max):
    count = 0
    a, b = 0, 1
    while count < max:
        yield b
        a, b = b, a + b
        count += 1
        
for n in fib_list(10000):
    print(n)
    
for n in fib_gen(10000):
    print(n)