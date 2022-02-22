def run(prime: int) -> bool:
    """
    Checks if the given prime is a palindrome arithmetically.
    Returns boolean.
    """

    if prime < 10:
        return True

    # saving prime to variable n to check if n == reverse
    n = prime

    # variable to track reversed prime value
    rev = 0

    # since we are using floor division for prime, we iterate until prime <= 0
    while prime > 0:

        # the currect digit being worked on is the remainder from mod 10, giving us the last digit
        dig = prime % 10

        # multiply current reverse by 10 to allow for addition of dig
        rev = (rev * 10) + dig

        # floor division on prime to truncate last digit
        prime = prime // 10

    # if n, the starting prime, is equal to the reverse then it is a palindrome
    if n == rev:
        return True
    else:
        return False
