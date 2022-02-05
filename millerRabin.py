from random import randrange


def evaluate(n: int, t: int) -> bool:
    """
    n: number to be evaluated
    t: number of test iterations
    Function for running the Miller-Rabin primality test.
    Will run the test t times.
    Returns a boolean showing that n is either composite or probably prime.
    """

    for _ in range(t):
        if not __primality(n):
            return False

    return True


def __primality(n: int) -> bool:
    """
    Operational code block of the Miller-Rabin primality test.
    Given an integer, n, will determine if composite or probably prime.
    """

    if n > 2 and n % 2 == 0:
        return False  # n is even

    # we will halve m iteratively until we achieve the equality:
    # n - 1 = (2^k)m
    k = 0
    m = n - 1

    # this loop halves m
    while m % 2 == 0:
        k += 1
        m //= 2  # floor div

    # we now have k, m such that m is an odd integer

    # determining random test value in range [2, n - 1]
    a = randrange(2, n - 1)

    # getting initial value for b
    b = pow(a, m, n)

    # initial check for primality
    if b == 1 or b == n - 1:
        return True

    # iterate until a result is found
    for _ in range(k - 1):

        # raising b^2 and getting remainder from modulo n
        b = pow(b, 2, n)

        # checking value of remainder against results
        if b == n - 1:
            return True
        elif b == 1:
            return False
