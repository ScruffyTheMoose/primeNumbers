import numpy as np


def sieve(n: int) -> list:
    """Sieve of Eratosthenes function. Give a value, n, and it will return a sorted list containing all primes in range [1, n+1]"""

    # set for tracking composite numbers
    composite_set = set()

    # set for tracking prime numbers
    prime_set = set()

    # for all elements in the range n starting with first prime
    for i in range(2, n + 1):

        # if i is not a composite number
        if i not in composite_set:

            # add i to the prime set
            prime_set.add(i)

            # for all elements from i^2 to n+1 stepping i values at a time
            # by going i values each iteration, it adds only multiples of i to the composite set
            # any values that it skips will by default be primes
            for j in range(i * i, n + 1, i):
                composite_set.add(j)

    result = list(prime_set)
    result.sort()  # python doesn't like converting a set to a list and sorting on the same line
    return result


def sieveBool(n: int) -> list:
    """Sieve of Eratosthenes that uses a list of boolean values rather than integers in order to be more memory efficient."""

    bools = np.full(n + 1, True)
    bools[0] = False
    bools[1] = False
    i = 2  # Start at 2 since 0 and 1 are not primes

    while i * i <= n:
        # If prime[i] is not changed, then it is a prime
        if bools[i]:
            # Update all multiples of i as False
            for j in range(i ** 2, n + 1, i):
                bools[j] = False
        # Check next number
        i += 1

    results = list()

    for i in range(n + 1):
        if bools[i]:
            results.append(i)

    return results
