from util.global_util import swap, compare_included

def partition(array: list, start: int, end: int, asc: bool):
    pivot = array[end]
    i = start

    for j in range(start, end):
        if compare_included(not asc, array[j], pivot):
            swap(array, j, i)
            i += 1

    swap(array, i, end)
    
    return i

def quick_sort(array_to_sort: list, start = 0, end = None, asc = True):
    array = array_to_sort

    if end is None:
        end = len(array_to_sort) - 1
        array = array_to_sort.copy()

    if start < end:
        p = partition(array, start, end, asc=asc)
        quick_sort(array, start, p - 1, asc=asc)
        quick_sort(array, p + 1, end, asc=asc)

    return array
