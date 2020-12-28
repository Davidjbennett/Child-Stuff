# Adapted from Perkovic, page 457: Counts primes in different ranges of 100,000 numbers
# This version uses a Process Pool

from time import perf_counter
from math import sqrt
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from os import getpid

starts = [12345678, 23456789, 34567890, 45678901, 56789012, 67890123, 78901234, 89012345]

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
    print(start,getpid(),flush=True)    # Remove this line to save time
    return sum(1 for i in range(start,start+100000) if isprime(i))

# Launching processes MUST be in a __main__ block! (But the functions called must not be!)
# The module is imported by each the process to access the functions. Hence main code only
# runs form the top-level module instance.
if __name__ == '__main__':
    print(cpu_count())
    start = perf_counter()
    with ProcessPoolExecutor(cpu_count()) as p:
        counts = p.map(countPrimes,starts)
    print(list(counts))
    stop = perf_counter()
    print(stop - start)

''' Output:
4
12345678 69214
23456789 69215
34567890 69217
45678901 69216
56789012 69214
67890123 69215
78901234 69217
89012345 69216
[6185, 5900, 5700, 5697, 5551, 5572, 5462, 5469]
5.1790637969999995
'''