import random


def primality(n: int) -> int:
    """Uses the Miller-Rabin test to determine with relatively high probability if a number is prime."""

    # if the number is greater than 2 and even, it is composite by default
    if n > 2 and n % 2 == 0:
        return 0

    s = 0
    t = n - 1

    while t % 2 == 0:
        s += 1
        t = t / 2

    # choosing a random x value in range [1, n-1]
    x = random.randint(1, n - 1)

    for i in range(1, s):
        if x ^ ((2 ^ i) * t) % n == 1 and x ^ ((2 ^ (i - 1)) * t) % n:
            return 0

    return 1


print(primality(31))
