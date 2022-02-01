def primality(n: int) -> list:
    """Testing Fermat's Primality test to see how accurate it is at identifying prime numbers."""

    # set for storing identified primes
    prime_set = set()

    # number of squares performed
    k = 0

    # variable for tracking the last prime used
    # initialized as 2, value will be updated dynamically as primes are found
    last_prime = 2

    # variable for holding and checking the current value for primality
    hold = 2

    while hold != n:
        
        hold *= 2
        k += 1

        if hold > n:
            hold = hold % n

            if hold % 2 != 0 and hold % 3 != 0:
                prime_set.add(hold)
                print(hold)

    return prime_set

def test():
    # p starts as an odd number
    p = 3

    for i in range(1, 10):
        if p % 5 == 3:
            pex = 2^(p - 1)

            if pex % p == 1 % p:
                print(p)
            else:
                print('nah fam')