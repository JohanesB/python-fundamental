def func_one(n):
    return [str(num) for num in range(n)]
funcc_one = func_one(10)
print(funcc_one)

def func_two(n):
    return list(map(str, range(n)))
funcc_two = func_two(10)
print(funcc_two)

import time

# CURRENT TIME BEFORE 
start_time = time.time()
# RUN CODE
result = func_one(1000000)
# CURRENT TIME AFTER RUNNING CODE
end_time = time.time()
# ELAPSED TIME
elapsed_time = end_time - start_time
print(elapsed_time)

# CURRENT TIME BEFORE 
start_time = time.time()
# RUN CODE
result = func_two(1000000)
# CURRENT TIME AFTER RUNNING CODE
end_time = time.time()
# ELAPSED TIME
elapsed_time = end_time - start_time
print(elapsed_time)

import timeit

stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt, setup, number = 100000))