from math import sqrt, floor

def sieve_eratosthenes(limit: int):
    max_check = floor(sqrt(limit))

    values = list(range(2, limit))

    for actual in values[0:max_check + 1]:
        values = list(filter(lambda x: x == actual or x % actual != 0, values))

    return values
