def sequential_search(arr: list, value):
    for key, item in enumerate(arr):
        if item == value:
            return key

    return -1

print(sequential_search([1, 2, 3, 4, 5, 6], 6))
