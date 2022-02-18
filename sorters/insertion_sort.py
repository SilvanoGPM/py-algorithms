def insertion_sort(array_to_sort: list, asc = True):
    array = array_to_sort.copy()
    n = len(array)

    for i in range(1, n):
        current = array[i]
        j = i - 1

        while (j >= 0 and (current < array[j] if asc else current > array[j])):
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current

    return array
