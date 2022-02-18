# Quando o valor da flag *asc* é True, compara se o valor na posição *index*
# é maior que a posição do valor atual, caso contrário, verifica se é menor.
def swap(arr: list, x: int, y: int):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


def compare(asc: bool, x, y):
    return x > y if asc else x < y
