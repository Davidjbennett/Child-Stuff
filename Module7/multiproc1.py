# multiproc1.py: Illustrate parallel processes

from multiprocessing import Process
import time

def fib(n):
    last,curr = 0,1
    return n if n in (last,curr) else fib(n-1) + fib(n-2)
    
if __name__ == '__main__':  # This is important! (Launched process imports this module)
    # First, do serial calls
    start = time.perf_counter()
    for n in range(10):
        fib(31)
    stop = time.perf_counter()
    print('serially:',stop-start)
    
    # Now in parallel (there will be some blocking, since 10 > #cpus)
    procs = []
    start = time.perf_counter()
    for n in range(10):
        proc = Process(target=fib,args=(31,))
        procs.append(proc)  # Keep process object to join later
        proc.start()        # Launch process
    for proc in procs:
        proc.join()         # Wait for each process to finish
    stop = time.perf_counter()
    print('concurrently:',stop-start)

'''
serially: 9.321782736
concurrently: 5.4984390990000005
'''