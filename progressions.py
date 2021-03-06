def arithmeticProg(primes: list, step_size: int = 30) -> dict:
    """
    Takes a list of prime numbers and uses it as a reference to check different arithmetic progressions for prime numbers.
    Checks for arithmetic progressions that are multiples of 30 by default.
    Returns a dictionary where key: value is 'start_point': 'step_size'
    """

    sequences = dict()
    prime_set = set(primes)

    # iterating through every prime in the given list to test all sequences starting at that value
    for prime in primes[3:]:

        # list for storing the sequence which we will then check for primes starting with the first prime
        sequence_list = [prime]

        # finding next element in arithmetic sequence starting from i with steps of 30 as specified by the prof
        # we only check up to the point that the last element in the sequence will be equal to the greatest prime we know
        next_element = -1
        i = 1

        while next_element <= primes[-1]:

            # getting next in sequence
            next_element = prime + (step_size * i)

            # increment i
            i += 1

            # if next_element is a prime, we add it to the list
            # if not, we stop the sequence
            if next_element in prime_set:
                sequence_list.append(next_element)
            else:
                break

        # checking if any primes were found
        if len(sequence_list) <= 1:
            pass
        else:
            # storing the resulting list of all primes found in the sequence in the sequences dictionary.
            # values are assigned to the key of the prime number
            sequences[prime] = sequence_list

    # returning a dict containg needed values
    return sequences


def llap(primes: list, step_size: int) -> dict:
    """Applies the arithmeticProg() algorithm and parses/returns the longest sequence identified."""

    # calling arithmeticProg() to build the set of all possible sequences based on given params
    sequences = arithmeticProg(primes, step_size=step_size)

    # finding the longest sequence in the set
    longest = -1
    for key in sequences.keys():

        # the length of the sequence being checked
        length = len(sequences[key])

        # comparing this length to previous best
        if length > longest:
            longest = length

    # dict for storing the details of the largest identified sequences
    results = {"length": longest, "step": step_size, "total": 0}

    # pulling all sequences that are longest length
    for key in sequences.keys():

        # if the sequence matches longest length, store in results
        if len(sequences[key]) >= longest:

            # commenting out full dict of sequences, inefficient and unnecessary for now
            # results[key] = sequences[key]
            results["total"] += 1

    return results
