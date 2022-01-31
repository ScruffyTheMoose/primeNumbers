def arithmeticProg(primes: list) -> dict:
    """
    Takes a list of prime numbers and uses it as a reference to check different arithmetic progressions for prime numbers.
    Checks only for arithmetic progressions that are multiples of 30.
    Returns a dictionary where key: value is 'step-size': 'primes'
    """

    prime_set = set(primes)

    result = dict()

    # iterating through every prime in the given list to test all sequences starting at that value
    for prime in primes:
        
        # list for storing the sequence which we will then check for primes starting with the first prime
        sequence_list = [prime]

        # finding next element in arithmetic sequence starting from i with steps of 30 as specified by the prof
        # we only check up to the point that the last element in the sequence will be equal to the greatest prime we know
        for i in range(1, len(primes) / 30):
            next_element = prime + (30 * i)

            # if next_element is a prime, we add it to the list
            if next_element in prime_set:
                sequence_list.append(next_element)

        # checking if any primes were found
        if len(sequence_list) <= 1:
            pass
        else:
            # need a line to iterate through the list in steps of 30 and find the most common
            pass

        # storing the resulting list of all primes found in the sequence in the result dictionary.
        # values are assigned to the key of the prime number
        result[prime] = sequence_list