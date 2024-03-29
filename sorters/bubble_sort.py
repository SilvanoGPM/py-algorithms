from util.sort_util import compare, swap

def bubble_sort(array_to_sort: list, asc = True):
    array = array_to_sort.copy()

    n = len(array) - 1

    for x in range(n):
        for i in range(n - x):            
            if compare(asc, array[i], array[i + 1]):
                swap(array, i, i + 1)
                
    return array
