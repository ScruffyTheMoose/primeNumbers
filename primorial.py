def run(primeList: list) -> list:
    """
    The standard primorial function.
    Runs until the nth prime in the list.
    Returns a sorted list containing the total product at each nth prime in the given list.
    Intended for use plotting the subsequent products.
    """

    # list for storing the product at each nth prime
    products = list()

    # initiating var to store product
    lastProd = 1

    # iterating through all primes in the list
    for prime in primeList:

        # getting product
        current = prime * lastProd

        # storing to list
        products.append(current)

        # updating product
        lastProd = current

        i += 1

    return products
