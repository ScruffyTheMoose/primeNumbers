from random import randrange


def run(n: int, t: int) -> bool:
    """
    n: number to be evaluated
    t: number of test iterations
    Function for running the Miller-Rabin primality test.
    Will run the test t times.
    Returns a boolean showing that n is either composite or probably prime.
    """

    if n == 2 or n == 3:
        return True

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

    for _ in range(t):

        # determining random test value in range [2, n - 1]
        a = randrange(2, n - 1)

        # getting initial value for b
        b = pow(a, m, n)

        # initial check for primality
        if b == 1 or b == n - 1:
            continue

        # iterate until a result is found
        for _ in range(k - 1):

            # raising b**2 and getting remainder from modulo n
            b = pow(b, 2, n)

            # checking value of b
            if b == n - 1:
                break

        # if inner loop ends, check reason for ending
        # loop was broken
        if b == n - 1:
            continue
        # loop ran out
        else:
            return False

    # if all iterations were completed without throwing False, then n is probably prime
    return True
