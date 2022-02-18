from util.global_util import compare

def merge(array: list, start: int, middle: int, end: int, asc: bool):
    left = array[start:middle]
    right = array[middle:end] 

    left_top = 0
    right_top = 0

    for i in range(start, end):
        # Caso a esquerda ou direita passem do tamanho de suas lista,
        # devemos preencher com o que resta na lista ao lado.
        left_extrapolate = left_top >= len(left)
        right_extrapolate = right_top >= len(right)

        if left_extrapolate:
            array[i] = right[right_top]
            right_top += 1
        elif right_extrapolate:
            array[i] = left[left_top]
            left_top += 1
        elif compare(not asc, left[left_top], right[right_top]):
            array[i] = left[left_top]
            left_top += 1
        else:
            array[i] = right[right_top]
            right_top += 1

def merge_sort(array_to_sort: list, start = 0, end = None, asc = True):
    array = array_to_sort
    
    if end is None:
        end = len(array_to_sort)
        array = array_to_sort.copy()

    can_resolve = end - start == 1

    if not can_resolve:
        middle = (start + end) // 2

        # Resolve a primeira metade da lista
        merge_sort(array, start, middle, asc=asc)

        # Resolve a segunda metade da lista
        merge_sort(array, middle, end, asc=asc)

        merge(array, start, middle, end, asc=asc)
            
    return array
