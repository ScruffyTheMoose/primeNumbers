def run(n):
    # This function uses the fibonacci test to test determine the input n's primality

    # First we generate the Fibonacci sequence mod n
    # No more than 4 entries are stored at a time for memory
    fib_seq = [0, 1, 1]
    i = 3
    while i <= n + 1:
        next_element = (fib_seq[-1] + fib_seq[-2]) % n
        fib_seq.append(next_element)
        del fib_seq[0]
        i += 1

    # Then we test if the n+1th term or the n-1th of the sequence is divisible by n
    # If yes, n is prime. Otherwise, n is composite
    if (fib_seq[-1] == 0) or (fib_seq[0] == 0):
        return True
    return False
