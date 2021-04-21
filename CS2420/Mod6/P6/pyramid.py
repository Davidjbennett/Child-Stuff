'''Pyramid class creates a pyramid of weights following the rules
of pascals triangle. The two people to the upper left and right of
a person half their weight and add it to the person below'''
import time
from hashmap import HashMap

FUNC_CALLS = 0
weight_cache = HashMap()


def weight_on(row,col):
    '''weight on does the math of calculating how much weight
    each person has on them'''
    global FUNC_CALLS
    FUNC_CALLS += 1
    if row <= 0:
        return 0
    if col < 0 or col > row:
        return 0
    result = 0
    if col > 0:
        result += 100 + weight_on(row - 1, col - 1) / 2
    if col <= row - 1:
        result += 100 + weight_on(row - 1, col) / 2
    return result

def weight_on_cached(row,col):
    '''weight on does the math of calculating how much weight
    each person has on them'''
    global FUNC_CALLS
    global weight_cache
    FUNC_CALLS += 1
    if row <= 0:
        return 0
    if col < 0 or col > row:
        return 0
    result = 0
    if col > 0:
        weight = 0
        try:
            weight = weight_cache.get((row-1,col-1))
            FUNC_CALLS += 1
        except:
            weight = weight_on_cached(row-1, col-1)/2
            weight_cache.set((row-1,col-1), weight)
        result += 100 + weight
    if col <= row - 1:
        weight = 0
        try:
            weight = weight_cache.get((row-1,col))
            FUNC_CALLS += 1
        except:
            weight = weight_on_cached(row-1, col)/2
            weight_cache.set((row-1,col), weight)
        result += 100 + weight
    return result

def main():
    '''main writes to part2.txt when not using a cache and again when using a cache'''
    global FUNC_CALLS
    depth = sys.argv[1]
    # depth = 20

    result = ""
    FUNC_CALLS = 0
    start = time.perf_counter()
    for row in range(depth):
        for col in range(row + 1):
            result +=  "{:.2f}".format(weight_on(row,col)) + " "
        result += "\n"
    end = time.perf_counter()
    print(result)
    print(f"Not chached: Elapsed time: {end-start:.10f} seconds. Number of function calls: {FUNC_CALLS}")
    fyle = open("CS2420\\Mod6\\P6\\part2.txt", "w")
    fyle.write(result + "\n" + f"Not Cached: Elapsed time: {end-start:.10f} seconds. Number of function calls: {FUNC_CALLS}\n\n")
    fyle.close()

    result = ""
    FUNC_CALLS = 0
    start = time.perf_counter()
    for row in range(depth):
        for col in range(row+1):
            result += "{:.2f}".format(weight_on_cached(row, col)) + " "
        result += '\n'
    end = time.perf_counter()
    print(result)
    print(f"Cached: Elapsed time: {end-start:.10f} seconds. Number of function calls: {FUNC_CALLS}")
    fyle2 = open("CS2420\\Mod6\\P6\\part3.txt", "w")
    fyle2.write(result + "\n" + f"Cached: Elapsed time: {end-start:.10f} seconds. Number of function calls: {FUNC_CALLS}\n\n")
    fyle2.close()

if __name__ == "__main__":
    main()
