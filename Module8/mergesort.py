# Source: https://www.geeksforgeeks.org/merge-sort/

def mergesort(arr, comparator): 
    if len(arr) >1: 
        # Sort halves ito separate memory
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L, comparator)
        mergesort(R, comparator)

        # Merge L and R back into arr 
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if comparator(L[i], R[j]): 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any elements were left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

alist = [4,3,7,1,9]
mergesort(alistn lambda x,y: x < y)
print(alist)        # [1, 3, 4, 7, 9]
