from random import randrange
import numpy as np

## NOTES ##
# Compare results against Prime Number Theorem.
# How many primes are found in the examined interval compared to what PNT suggests should exist.


########## High Digit Sieve ##########
def run(sieve_primes: list, l: int, u: int, t: int) -> list:
    """
    sieve_primes: a list of trivial primes to sieve out majority of composite numbers in high digit range
    l: lower bound of interval
    u: upper bound of interval
    t: number of tests to iterate on each potential prime

    t=1 conducts single Fermat test
    t=60 for error rate of 2^(-128)
    """

    # ensuring boundaries are odd
    if l % 2 == 0:
        l -= 1
    if u % 2 == 0:
        u += 1

    shape = int((u - l) / 2)
    bools = np.full(shape, None)
    i = 0

    # iterating through only odd numbers on interval
    for n in range(l, u, 2):

        # initially assumed to be prime
        stat = True

        # checking if any prime factors exist for n
        # starts at smallest primes which are most probable
        for p in sieve_primes:

            # if p is a factor of n, we know its composite and exit check
            if n % p == 0:
                stat = False
                break

        # if all prime factor checks completed, run Miller-Rabin and store result
        if stat:
            bools[i] = _mr(n, t)
        # if prime factor checks failed, store result immediately
        else:
            bools[i] = stat

        # increment i
        i += 1

    # list of resulting primes
    primes = list()
    # iterator variable
    j = 0

    # cross checking elements in interval against boolean results
    for n in range(l, u, 2):

        if bools[j] == True:
            primes.append(n)

        j += 1

    return primes


########## Miller-Rabin Test ##########
# This code has been duplicated from the millerRabin.py module to avoid requiring imports when sharing with the team.
def _mr(n: int, t: int) -> bool:
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

    # ensuring atleast 1 test iteration is run
    if t <= 0:
        t += 1

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
