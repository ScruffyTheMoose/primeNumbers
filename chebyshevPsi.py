from math import log, pow

####### UNFINISHED ########


def run(primeList: list, n: int) -> list:
    """
    Chebyshev's Psi function.
    Runs until the nth prime in the list.
    Returns a sorted list containg all Psi(x) values until n.
    Intended for use plotting the subsequent terms.
    """

    # checking n is within bounds
    m = n
    if n > len(primeList) or n < 1:
        m = len(primeList)

    x = primeList[m]

    results = list()

    for k in range(m + 1):

        tot = 0

        for z in range(0, len(primeList)):

            pk = pow(primeList[z], k)

            if pk > x:
                continue

            current = log(primeList[z])

            tot += current

        results.append(tot)

    return results
