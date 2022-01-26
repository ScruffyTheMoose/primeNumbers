import pandas as pd

def sieve(n: int) -> list:
    """Sieve of Eratosthenes function. Give a value, n, and it will return a sorted list containing all primes in range [1, n+1]"""
    
    # set for tracking composite numbers
    composite_set = set()

    # set for tracking prime numbers
    prime_set = set()

    # for all elements in the range n starting with first prime
    for i in range(2, n+1):

        # if i is not a composite number
        if i not in composite_set:

            # add i to the prime set
            prime_set.add(i)

            # for all elements from i^2 to n+1 stepping i values at a time
            # by going i values each iteration, it adds only multiples of i to the composite set
            # any values that it skips will by default be primes
            for j in range(i*i, n+1, i):
                composite_set.add(j)

    result = list(prime_set)
    result.sort() # python doesn't like converting a set to a list and sorting on the same line
    return result

def sieveToCSV(n: int, column_name: str, file_name: str) -> None:
    """Sieve of Eratosthenes function. Give a value, n, and it will find all primes in range [1, n+1] and save the results to a CSV file."""
    
     # set for tracking composite numbers
    composite_set = set()

    # set for tracking prime numbers
    prime_set = set()

    # for all elements in the range n starting with first prime
    for i in range(2, n+1):

        # if i is not a composite number
        if i not in composite_set:

            # add i to the prime set
            prime_set.add(i)

            # for all elements from i^2 to n+1 stepping i values at a time
            # by going i values each iteration, it adds only multiples of i to the composite set
            # any values that it skips will by default be primes
            for j in range(i*i, n+1, i):
                composite_set.add(j)

    result = list(prime_set)
    result.sort()
    
    # writes list to dataframe with column labeled as list_name and saves to file_name
    pd.DataFrame(result, columns=[column_name]).to_csv(path_or_buf=f'{file_name}.csv')