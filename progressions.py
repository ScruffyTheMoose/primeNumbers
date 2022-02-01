def arithmeticProg(primes: list, step_size: int = 30) -> dict:
    """
    Takes a list of prime numbers and uses it as a reference to check different arithmetic progressions for prime numbers.
    Checks for arithmetic progressions that are multiples of 30 by default.
    Returns a dictionary where key: value is 'start_point': 'step_size'
    """

    sequences = dict()
    result = dict()
    prime_set = set(primes)
    
    # covering all starting points based on step_size. Once we reach n + step_size, the values begin to repeat.
    test_range = list()
    for n in range(7, 7 + step_size):
        if n in prime_set:
            test_range.append(n)

    # iterating through every prime in the given list to test all sequences starting at that value
    for prime in test_range:
        
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
            if next_element in prime_set:
                sequence_list.append(next_element)

        # checking if any primes were found
        if len(sequence_list) <= 1:
            pass
        else:
            # storing the resulting list of all primes found in the sequence in the sequences dictionary.
            # values are assigned to the key of the prime number
            sequences[prime] = sequence_list
            
    return sequences

############### UNFINISHED ##################
def __longestSequence(input: list) -> int:
    """Finds the most frequently occurring step amongst all of the elements of the input list and returns the value."""
    
    # list for storing the gaps
    delta_list = list()
    result = list()
    
    # iterates through the first half of the sequence
    for i in range(0, len(input) // 2):
        
        # compares the element to every other element in the first half to find the difference
        for j in range(i + 1, len(input) // 2):
            
            # stores the difference in delta_list
            delta = abs(input[i] - input[j])
            delta_list.append(delta)
            
    # creates set of the counts for each gap and finds the most frequently occurring
    freq_delta = max(set(delta_list), key=delta_list.count)
        
    return freq_delta