# Adapted from Perkovic, page 457: Counts primes in different ranges of 100,000 numbers
from time import perf_counter
from math import sqrt

starts = [12345678, 23456789, 34567890, 45678901, 56789012, 67890123, 78901234, 890123451]

def isprime(n):
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False    # Number not odd; can't be prime
    for x in range(3, int(sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True
    
def countPrimes(start):
    return sum(1 for i in range(start,start+100000) if isprime(i))

start = perf_counter()
counts = map(countPrimes,starts) 
print(list(counts))
stop = perf_counter()
print(stop - start)

''' Output:
[6185, 5900, 5700, 5697, 5551, 5572, 5462, 5469]
12.722695511
'''