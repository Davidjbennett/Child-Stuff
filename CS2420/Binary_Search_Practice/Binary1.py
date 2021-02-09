import random
import time
import math

randomSample = random.sample(range(2000), 1000)
sortedSample = randomSample.sort()

def Binary_Search(lyst, target):
    midpoint = len(lyst) // 2

    if lyst[midpoint] == target:
        return True
    elif lyst[len(lyst) - 1] < target:
        return False
        
    if target < lyst[midpoint]:
        return Binary_Search(lyst[:midpoint], target)
    elif target > lyst[midpoint]:
        return Binary_Search(lyst[midpoint+1:], target)



def main():
    lyst = [0,1,2,3,4,5,6,7,8,9]
    print(Binary_Search(lyst, 11))

if __name__ == '__main__':
    main()
