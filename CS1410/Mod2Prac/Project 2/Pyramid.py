import sys
from time import perf_counter

WEIGHT = 200

cache = {}

numberOfFunctionCalls = 0
numberOfCacheCalls = 0

def weightOn(r, c):
    global numberOfFunctionCalls
    numberOfFunctionCalls += 1
    
    global numberOfCacheCalls
    if(r,c) in cache:
        numberOfCacheCalls += 1
        return cache[(r,c)]
    if r == 0:
        result = 0.0
    elif c == 0:
        result = (WEIGHT + weightOn(r - 1, 0))/2.0
    elif r == c:
        result = (WEIGHT + weightOn(r - 1, c-1))/2.0
    else:
        result = WEIGHT + (weightOn(r-1, c-1) + weightOn(r-1, c))/2.0
    
    cache[(r,c)] = result

    return result


def main():
    rows = int(sys.argv[1])

    with open("part3.txt", 'w') as f:
        start = perf_counter()

        for i in range(rows):
            for j in range(i+1):
                print(f'{weightOn(i, j):.2f}', file=f, end = " ")
            print(file=f)
        
        end = perf_counter()
        
        print(file = f)
        print(f"Elapsed Time: {end - start:.20f}", file=f)
        print(f"Number of functions calls: {numberOfFunctionCalls}", file=f)
        print(f"Number of cache calls: {numberOfCacheCalls}", file=f)

    

if __name__ == "__main__":
    main()
