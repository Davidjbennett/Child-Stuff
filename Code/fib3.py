''' fib3.py: A recursive fib w/o caching '''

def fib(n):
    return n if n in (0,1) else fib(n-1) + fib(n-2)

print(fib(35))
