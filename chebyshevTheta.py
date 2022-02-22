from math import log


def run(primeList: list) -> list:
    """
    Chebyshev's Theta Function.
    Returns a sorted list containing the log transformed product of the primorial at each prime in the given list.
    """

    # list for storing the product at each nth prime
    products = list()

    # initiating var to store current Theta(x)
    lastVal = 0

    # iterating through all primes in the list
    for prime in primeList:

        # getting sum of logs
        # using log laws, we know log(n) + log(m) == log(nm)
        current = log(prime) + lastVal

        # storing to list
        products.append(current)

        # updating product
        lastVal = current

    return products
