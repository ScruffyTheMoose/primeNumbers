from re import L
import millerRabin as mr
import pandas as pd


def run(sieve_primes: list, l: int, u: int, t: int) -> list:
    """
    sieve_primes: a list of trivial primes to sieve out majority of composite numbers in high digit range
    l: lower bound of interval
    u: upper bound of interval
    t: number of tests to iterate on each potential prime

    t=0 conducts single Fermat test
    t=60 for error rate of 2^(-128)
    """

    # ensuring boundaries are odd
    if l % 2 == 0:
        l -= 1
    if u % 2 == 0:
        u += 1

    # use binary search to find closest divisor between sieve_primes and the interval
    # since the lists are sorted ascending it should work fairly quickly

    # iterating through only odd numbers on interval
    for i in range(l, u, 2):
        pass
