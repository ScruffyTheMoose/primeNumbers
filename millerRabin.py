from random import randrange


def evaluate(n: int, t: int) -> bool:
    """
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
        False  # n is even

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
    if b == 1 or b == -1:
        return True

    # exponent for 2^s * m
    # in formula for recalculating b
    s = 0

    # iterate until a result is found
    while True:

        # raising b to (2^s)m and getting remainder from modulo n
        b = pow(b, pow(2, s) * m, n)

        # checking value of remainder against results
        if (b - n) == -1:
            return True
        elif b == 1:
            return False

        # if no result determined, increment s and repeat on b
        s += 1
