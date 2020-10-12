''' Computes the nth Fibonacci number procedurally (without recursion ) '''

from time import perf_counter

def fib(n):
    if n in (0,1):
        return n
    first,second = 1,1
    for n in range(2,n):
        first,second = second,first+second
    return second

start = perf_counter()
print(fib(35))
print(perf_counter() - start)

''' Output:
9227465
3.093799999999772e-05
'''
