from util.sort_util import swap

def revert_array(array_to_revert: list):
    array = array_to_revert.copy()

    n = len(array)
    limit = n // 2

    for i in range(limit):
        swap(array, i, n - i - 1)

    return array
