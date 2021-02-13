""" An assortment of various search algorithms
"""
import time
import random

def validate_numeric_array(lyst):
    """ This function makes sure a list holds only numerical values
    """
    for num in range(len(lyst)):
        if not str(lyst[num]).isdigit():
            raise ValueError
        return True


def is_sorted(lyst):
    """ This function test if a list is sorted and returns true if it is
    """
    result = True
    for num in range(1, len(lyst)):
        if lyst[num-1] > lyst[num]:
            result = False
    return result

def selection_sort(lyst):
    """This is a selection sort
    """
    for num in range(len(lyst)):
        for num2 in range(len(lyst)):
            if lyst[num] < lyst[num2]:
                lyst[num], lyst[num2] = lyst[num2], lyst[num]
    return lyst

def insertion_sort(lyst):
    """This is a insertion sort
    """
    # index = 0
    for num in range(1,len(lyst)):
        search = True
        index = num
        while search:
            if index == 0:
                search = False
            elif lyst[index-1] > lyst[index]:
                lyst[index-1], lyst[index] = lyst[index], lyst[index-1]
                index -= 1
            else:
                search = False
    return lyst

def mergesort(lyst):
    """This is a merge sort
    """
    if len(lyst) > 1:
        mid = len(lyst) // 2
        left_lyst = lyst[:mid]
        right_lyst = lyst[mid:]

        mergesort(left_lyst)
        mergesort(right_lyst)

        left_ind = 0
        right_ind = 0
        new_ind = 0

        while left_ind < len(left_lyst) and right_ind < len(right_lyst):
            if left_lyst[left_ind] < right_lyst[right_ind]:
                lyst[new_ind] = left_lyst[left_ind]
                left_ind += 1
            else:
                lyst[new_ind] = right_lyst[right_ind]
                right_ind += 1
            new_ind += 1

        while left_ind < len(left_lyst):
            lyst[new_ind] = left_lyst[left_ind]
            left_ind += 1
            new_ind += 1
        while right_ind < len(right_lyst):
            lyst[new_ind] = right_lyst[right_ind]
            right_ind += 1
            new_ind += 1
    return lyst
def quicksort(lyst):
    """This is a quicksort
    """
    def partition_helper(lyst, first, last):
        pivot = lyst[first]
        left = (first + 1)
        right = last
        done = False
        while not done:
            while left <= right and lyst[left] <= pivot:
                left += 1
            while right >= left and lyst[right] >= pivot:
                right -= 1
            if right < left:
                done = True
            else:
                lyst[left], lyst[right] = lyst[right], lyst[left]
        lyst[first], lyst[right] = lyst[right], lyst[first]
        return right
    def quicksort_helper(lyst, first, last):
        if first < last:
            splitpoint = partition_helper(lyst, first, last)

            quicksort_helper(lyst, first, (splitpoint-1))
            quicksort_helper(lyst, (splitpoint+1), last)
        return lyst
    quicksort_helper(lyst, 0, (len(lyst)-1))
    return lyst

def timsort(lyst):
    """This is the built in timsort
    """
    return sorted(lyst)

def main():
    """This main function calls, times, test if numeric, and test if sorted
    for all list.
    """
    random.seed(13)
    rand_lyst = random.sample(range(200), k=50)
    search_list = ["quicksort", "mergesort", "selection", "insertion", "timsort"]
    for num in range(len(search_list)):
        test_lyst = rand_lyst.copy()

        if search_list[num] == "quicksort":
            # print(test_lyst)
            if validate_numeric_array(test_lyst):
                print("Starting quicksort:")
                start = time.perf_counter()
                quicksort(test_lyst)
                end = time.perf_counter()
                print(f"List is sorted: {is_sorted(test_lyst)}")
                print(f"Time for quicksort: {end-start:.5f}\n")
            else:
                print("List is not numerical")
        elif search_list[num] == "mergesort":
            if validate_numeric_array(test_lyst):
                print("Starting mergesort:")
                start = time.perf_counter()
                mergesort(test_lyst)
                end = time.perf_counter()
                print(f"List is sorted: {is_sorted(test_lyst)}")
                print(f"Time for mergesort: {end-start:.5f}\n")
            else:
                print("List is not numerical")
        elif search_list[num] == "selection":
            if validate_numeric_array(test_lyst):
                print("Starting selection sort:")
                start = time.perf_counter()
                selection_sort(test_lyst)
                end = time.perf_counter()
                print(f"List is sorted: {is_sorted(test_lyst)}")
                print(f"Time for selection_sort: {end-start:.5f}\n")
            else:
                print("List is not numerical")
        elif search_list[num] == "insertion":
            if validate_numeric_array(test_lyst):
                print("Starting insertion sort:")
                start = time.perf_counter()
                insertion_sort(test_lyst)
                end = time.perf_counter()
                print(f"List is sorted: {is_sorted(test_lyst)}")
                print(f"Time for insertion_sort: {end-start:.5f}\n")
            else:
                print("List is not numerical")
        elif search_list[num] == "timsort":
            if validate_numeric_array(test_lyst):
                print("Starting timsort:")
                start = time.perf_counter()
                timsort(test_lyst)
                end = time.perf_counter()
                print(f"List is sorted: {is_sorted(timsort(test_lyst))}")
                print(f"Time for timsort: {end-start:.5f}\n")
            else:
                print("List is not numerical")

if __name__ == "__main__":
    main()
