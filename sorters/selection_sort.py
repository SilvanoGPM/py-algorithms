def get_index(array: list, start = 0, asc = True):
    index = start

    for i in range(start, len(array)):
        comparation = array[i] < array[index] if asc else array[i] > array[index]
        
        if (comparation):
            index = i

    return index


def selection_sort(array_to_sort: list, asc = True):
    array = array_to_sort.copy()

    for i in range(len(array) - 1):
        index = get_index(array, i, asc=asc)

        # Quando o valor da flag *asc* é True, compara se o valor na posição *index*
        # é maior que a posição do valor atual, caso contrário, verifica se é menor.
        comparation = array[i] > array[index] if asc else array[i] < array[index]

        if (comparation):
            temp = array[i]
            array[i] = array[index]
            array[index] = temp


    return array

