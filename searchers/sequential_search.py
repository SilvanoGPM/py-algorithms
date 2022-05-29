def sequential_search(arr: list, value):
    for key, item in enumerate(arr):
        if item == value:
            return key

    return -1
