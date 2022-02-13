def run(primeList: list, n: int) -> list:
    """
    The standard primorial function.
    Runs until the nth prime in the list.
    Returns a sorted list containing the total product at each nth prime in the given list.
    Intended for use plotting the subsequent products.
    """

    # checking n is within bounds
    k = n
    if n > len(primeList) or n < 1:
        k = len(primeList)

    # list for storing the product at each nth prime
    products = list()

    # initiating var to store product
    lastProd = 1

    # iterating through all primes in the list
    for i in range(k):

        # getting product
        current = primeList[i] * lastProd

        # storing to list
        products.append(current)

        # updating product
        lastProd = current

    return products
