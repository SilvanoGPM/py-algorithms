def bubble_sort(array_to_sort: list, asc = True):
    array = array_to_sort.copy()

    n = len(array) - 1

    for x in range(n):
        for i in range(n - x):
            comparation = array[i] > array[i + 1] if asc else array[i] < array[i + 1]
            
            if comparation:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                
    return array
