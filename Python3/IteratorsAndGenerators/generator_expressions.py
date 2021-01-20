import time

g = (num for num in range(1, 10))

print(next(g))
print(next(g))
print(next(g))
print(next(g))

gen_start_time = time.time()
print(sum(num for num in range(1, 10000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([num for num in range(1, 10000000)]))
list_time = time.time() - list_start_time

print(f"sum(num for num in range(1, 10000000)) tooK {gen_time}")

print(f"sum([num for num in range(1, 10000000)]) tooK {list_time}")