from math import sqrt, floor

def sieve_eratosthenes():
    limit = 30
    max_check = floor(sqrt(limit))

    values = list(range(2, limit))

    for actual in values[0:max_check + 1]:
        values = list(filter(lambda x: x == actual or x % actual != 0, values))

    return values

print(sieve_eratosthenes())
