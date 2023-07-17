def create_cubes(n):
    
    for x in range(n):
        yield x**3
    
print(list(create_cubes(10)))

def gen_fibon(n):
    x = 1
    y = 2

    for i in range(n):
        yield x
        x, y = y, x + y
for num in gen_fibon(10):
    print(num)