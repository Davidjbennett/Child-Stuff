import random
import time
import math

random.seed(13)
sampleLyst = random.sample(range(2000000), k=1000000)
sortedLyst = sampleLyst
sortedLyst.sort()

# print(sortedLyst[999000])
# print(len(sortedLyst))

def linear_search(lyst, target):
    if(len(lyst) == 0):
        return f"There are no items in your list"
    for i in lyst:
        if(target == i):
            return f"Target number {target} found."
    return f"{target} not found"

start = time.perf_counter()
print(linear_search(sampleLyst, 1998011))
end = time.perf_counter()
print(f"Time result for Linear search: {end-start:.6f}")


def binary_search(lyst, target):
    if(len(lyst) == 0):
        return f"There are no items in your list"
    midpoint = len(lyst) // 2
    if(lyst[midpoint] == target):
        return f"Target number {target} found."
    else:
        if(target < lyst[midpoint]):
            return binary_search(lyst[:midpoint], target)
        elif(target > lyst[midpoint]):
            return binary_search(lyst[midpoint+1:], target)
        else:
            return f"{target} not found."

start2 = time.perf_counter()
print(binary_search(sortedLyst, 1998011))
end2 = time.perf_counter()
print(f"Time result for Binary search: {end2-start2:.6f}")


def jump_search(lyst, target):
    block = 0
    step = int(math.sqrt(len(lyst)))
    notFound = True
    while(notFound):
        if(block > len(lyst)):
            return f"{target} not found."
        elif(lyst[block] < target):
            block += step
        else:
            for i in lyst[block-step:block+1]:
                if(target == i):
                    return f"Target number {target} found at."

start3 = time.perf_counter()
print(jump_search(sortedLyst, 1998011))
end3 = time.perf_counter()
print(f"Time result for Jump search: {end3-start3:.6f}")

