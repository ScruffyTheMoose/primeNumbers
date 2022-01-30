def maxDelta(primes: list) -> dict:
    """Will take a sorted list of integers and determine the greatest gap between two consecutive values in the list. Returns a dictionary containing the the two values and the size of the gap."""
    
    # maximum is a variable for tracking the largest gap found. If a gap is greater than maximum, the value will be updated.
    maximum = 0
    
    # values is a variable for tracking the two numbers where the gap occurs.
    values = [0, 0]
    
    # this for-loop will iterate through all of the numbers in the list that is given as an argument
    # as we iterate through the list, we compare the number at the current index (i) to the number at the next index (i + 1)
    for i in range(0, len(primes) - 1):
        
        # n is a variable storing the number at index 'i'
        n = primes[i]
        
        # m is a variable storing the number at index 'i + 1'
        m = primes[i + 1]
        
        # delta is just the absolute value of the difference between n and m
        delta = abs(m - n)
        
        # if delta is greater than the current maximum gap, than:
        if delta > maximum:
            
            # maximum is updated to the new maximum gap
            maximum = delta
            
            # values is updated to store the two numbers where the gap occurs
            values = [n, m]
            
    # lastly, we return a dictionary which stores key:value valuess
    # 'primes' stores the two numbers were the gap occured
    # 'gap' stores the size of the gap
    return {'primes': values, 'gap': maximum }