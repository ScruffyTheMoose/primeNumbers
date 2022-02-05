![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)


`primeNumbers` is a research repository being built as part of an undergraduate research team studying patterns and relationships in prime numbers.

### millerRabin.py
A personal build of the Miller-Rabin probabilistic primality test. Using the evaluate() function, you can test any integer n for t iterations. False confirms that n is a composite number while True implies that the number is *probably* prime.
It is recommended to run between 40 and 60 tests for optimal evaluation of n.

### sieveOfEratosthenes.py
This module contains the modified version of the Sieve of Eratosthenes. Instead of using list to store prime and composite numbers, we use sets. Lists require O(n) time to check if an element exists in the list, wheras a set can perform the same operation in O(1) time. The overall function of the algorithm is the same but is able to be performed at a significantly faster speed. At the end of the function, the set is converted to a list and sorted before being returned.

### progressions.py
A module built from scratch that can build arithmetic sequences of primes and determine the longest sequences identfied based on the provided parameters. The base algorithm in arithmeticProg() will return a dictionary containing all of the sequences built. Additionally, llap() will find and return the details of the longest sequences in the set.

### palindromes.py
Module that will take an integer value and determine whether or not it is a palindromic number. It will return boolean values 1 (True) or 0 (False) to denote whether or not the given number is a palindrome.

### maxDelta.py
A module for determining the greatest delta between two prime numbers in a given set. The function will return a dictionary with two elements; a list with the primes where the gap occured, and a value representing the size of the gap.

### palindromeStudy.ipynb
This is the jupyter notebook where the palindromes.py module was applied to sets of prime numbers and the results were evaluated.
