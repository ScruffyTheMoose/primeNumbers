from math import log


def run(primeList: list, n: int) -> list:
    """
    Chebyshev's Theta Function using natural log.
    Runs until the nth prime in the list.
    Returns a sorted list containing the log transformed product at each nth prime in the given list.
    Intended for use plotted the subsequent log transformed products.
    """

    # checking n is within bounds
    k = n
    if n > len(primeList) or n < 1:
        k = len(primeList)

    # list for storing the product at each nth prime
    products = list()

    # initiating var to store product
    lastVal = 0

    # iterating through all primes in the list
    for i in range(k):

        # getting sum of logs
        # using log laws, we know log(n) + log(m) == log(nm)
        current = log(primeList[i]) + lastVal

        # storing to list
        products.append(current)

        # updating product
        lastVal = current

    return products
