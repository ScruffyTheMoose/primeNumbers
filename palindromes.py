def palindrome(number: int) -> bool:
    """Checks if the given number is a palindrome arithmetically and returns a boolean."""

    # saving number to variable n to check if n == reverse
    n = number

    # variable to track reversed number value
    rev = 0

    # since we are using floor division for number, we iterate until number <= 0
    while number > 0:

        # the currect digit being worked on is the remainder from mod 10, giving us the last digit
        dig = number % 10

        # multiply current reverse by 10 to allow for addition of dig
        rev = (rev * 10) + dig

        # floor division on number to truncate last digit
        number = number // 10

    # if n, the starting number, is equal to the reverse then it is a palindrome
    if n == rev:
        return True
    else:
        return False
