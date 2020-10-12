''' fib3_perf.py: A recursive fib w/o caching '''

from time import perf_counter

def fib(n):
    return n if n in (0,1) else fib(n-1) + fib(n-2)

start = perf_counter()
print(fib(35))
print(perf_counter() - start)

''' Output:
9227465
4.316265319999999
'''