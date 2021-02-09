""" Linear, Binary, and Jump search algorithms """
import random
# import time
import math

random.seed(13)
sampleLyst = random.sample(range(2000), k=100)
sortedLyst = sampleLyst
sortedLyst.sort()

# print(sortedLyst[999000])
# print(len(sortedLyst))

def linear_search(lyst, target):
    ''' Linear search algorithm. Takes a list in lyst and
    searches for a target number.
    '''
    if len(lyst) == 0 :
        return "There are no items in your list"
    for i in lyst:
        if target == i :
            # return f"Target number {target} found."
            return "Target found"
    # return f"{target} not found"
    return "Target not found"

# start = time.perf_counter()
# print(linear_search(sortedLyst, 1998011))
# end = time.perf_counter()
# print(f"Time result for Linear search: {end-start:.6f}")


def binary_search(lyst, target):
    ''' binary search algorithm. Takes a sorted list in lyst and
    searches for a target number.
    '''
    if len(lyst) == 0:
        return "There are no items in your list"
    midpoint = len(lyst) // 2
    if lyst[midpoint] == target :
        # return f"Target number {target} found."
        return "Target found"
    else:
        if target < lyst[midpoint]:
            return binary_search(lyst[:midpoint], target)
        elif target > lyst[midpoint]:
            return binary_search(lyst[midpoint+1:], target)
        else:
            # return f"{target} not found."
            return "Target not found"

# start2 = time.perf_counter()
# print(binary_search(sortedLyst, 1998011))
# end2 = time.perf_counter()
# print(f"Time result for Binary search: {end2-start2:.6f}")


# def jump_search(lyst, target):
#     ''' jump search algorithm. Takes a sorted list in lyst and
#     searches for a target number.
#     '''
#     block = 0
#     step = int(math.sqrt(len(lyst)))
#     notFound = True
#     while notFound:
#         if block > len(lyst):
#             # return f"{target} not found."
#             return "Target not found"
#         if lyst[block] < target:
#             block += step
#         else:
#             for i in lyst[block-step:block+1]:
#                 if target == i:
#                     # return f"Target number {target} found."
#                     return "Target found"

def jump_search(lyst, target):
    ''' jump search algorithm. Takes a sorted list in lyst and
        searches for a target number.
    '''
    lystlen = len(lyst)
    step = math.sqrt(lystlen)
    prev = 0
    while lyst[int(min(step, lystlen))-1] < target:
        prev = step
        step += math.sqrt(lystlen)
        if prev >= lystlen:
            return "Target not found"
    while lyst[int(prev)] < target:
        prev += 1
        if prev == min(step, lystlen):
            return "Target not found"
    if lyst[int(prev)] == target:
        return "Target found"
    return "Target not found"


print(sortedLyst[99])
# start3 = time.perf_counter()
print(jump_search(sortedLyst, 1944))
# end3 = time.perf_counter()
# print(f"Time result for Jump search: {end3-start3:.6f}")
