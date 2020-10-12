''' fib2.py: Caches values of all calls '''

from time import perf_counter

cache = {}        # Save results as arg-value pairs

def fib(n):
    if n in (0,1): 
        result = n
    elif n in cache:
        result = cache[n]
    else:
        result = fib(n-1) + fib(n-2)
        cache[n] = result
    return result

start = perf_counter()
print(fib(35))
print(perf_counter() - start)
