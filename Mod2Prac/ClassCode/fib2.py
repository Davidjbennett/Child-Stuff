''' fib2.py: Caches values of all calls '''

cache = {}        # Save results as arg-value pairs

def fib(n):
    if n in (0,1): 
        result = n
    elif n in cache:
        result = cache[n]
        #print('fib(',n,') found in cache')
    else:
        result = fib(n-1) + fib(n-2)
        cache[n] = result
    return result

print(fib(30))


