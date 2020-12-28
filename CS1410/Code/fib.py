''' Computes the nth Fibonacci number procedurally (without recursion ) '''

def fib(n):
    if n in (0,1):
        return n
    first,second = 1,1
    for n in range(2,n):
        first,second = second,first+second
    return second

for i in range(0,10):
    print(fib(i))
