from util.sort_util import swap, compare

def get_index(array: list, start = 0, asc = True):
    index = start

    for i in range(start, len(array)):        
        if compare(not asc, array[i], array[index]):
            index = i

    return index


def selection_sort(array_to_sort: list, asc = True):
    array = array_to_sort.copy()

    for i in range(len(array) - 1):
        index = get_index(array, i, asc=asc)

        if compare(asc, array[i], array[index]):
            swap(array, i, index)

    return array
