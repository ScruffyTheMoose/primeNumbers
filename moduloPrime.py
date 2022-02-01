def primality(n: int) -> list:
    """Testing Fermat's Primality test to see how accurate it is at identifying prime numbers."""

    ############### UNFINISHED ################

    # set for storing identified primes
    prime_set = set()

    # number of squares performed
    k = 0

    # variable for tracking the last prime used
    # initialized as 2, value will be updated dynamically as primes are found
    last_prime = 2

    # variable for holding and checking the current value for primality
    hold = 2

    while k != n:
        
        hold *= 2
        k += 1

        if hold > n:
            hold = hold % n

            if hold % 2 != 0 and hold % 3 != 0:
                prime_set.add(hold)

    result = list(prime_set)
    result.sort()

    return result

# quick testing of function
print(primality(113))
