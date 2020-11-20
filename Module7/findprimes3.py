# Adapted from Perkovic, page 457: Counts primes in different ranges of 100,000 numbers
# This version uses a Thread Pool

from time import perf_counter
from math import sqrt
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor
from os import getpid
import threading

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
    print(start,threading.currentThread().getName(),flush=True)    # Remove this line to save time
    return sum(1 for i in range(start,start+100000) if isprime(i))

# Using a __main__ block not required for threads (there is only 1 process)
print(cpu_count())
start = perf_counter()
with ThreadPoolExecutor(cpu_count()) as p:
    counts = p.map(countPrimes,starts)
print(list(counts))
stop = perf_counter()
print(stop - start)

''' Output:
4
12345678 ThreadPoolExecutor-0_0
23456789 ThreadPoolExecutor-0_1
34567890 ThreadPoolExecutor-0_2
45678901 ThreadPoolExecutor-0_3
56789012 ThreadPoolExecutor-0_0
67890123 ThreadPoolExecutor-0_1
78901234 ThreadPoolExecutor-0_2
89012345 ThreadPoolExecutor-0_3
[6185, 5900, 5700, 5697, 5551, 5572, 5462, 5469]
13.005002092
'''