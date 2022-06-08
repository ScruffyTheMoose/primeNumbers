![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)


`primeNumbers` is a research repository being built as part of an undergraduate research team studying patterns and relationships in prime numbers.

## [View our Poster](https://raw.githubusercontent.com/ScruffyTheMoose/primeNumbers/main/imgs/MURL-poster-img.png) or [Read our Paper](https://github.com/ScruffyTheMoose/primeNumbers/blob/main/imgs/NumericalAdventuresWithPrimeNumbers.pdf)

### Studies Folder
This folder contains Jupyter Notebooks were I applied the algorithms built here to look for interesting patterns in sets of prime numbers.

### millerRabin.py
A personal build of the Miller-Rabin probabilistic primality test.
It is recommended to run between 40 and 60 tests for optimal evaluation of n.

```
# testing primality of number
millerRabin.run(53, 40)
```
```
# returns
True
```

### sieveOfEratosthenes.py
Two versions included with one using integers and one using booleans. It is recommended to use the boolean version for speed and memory efficiency.

```
# finding primes
sieveOfEratosthenes.runBool(10)
```
```
# returns
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

### progressions.py
A module built from scratch that can build arithmetic sequences of primes and determine the longest sequences in a range.

```
# finding progressions
progressions.arithmeticProg(primeList, 30)
```
```
# returns
{7: [7, 37, 67, 97],
 11: [11, 41, 71],
 13: [13, 43, 73],
 17: [17, 47],
 23: [23, 53, 83],
 .......
```

```
# finding longest progression
progressions.llap(primeList, 30)
```
```
# returns
{'length': 6, 'step': 30, 'total': 4}
```

### palindromes.py
Module that will take an integer value and determine whether or not it is a palindromic number. Should be applied iteratively.

```
# identifying palindrome
palindromes.run(11)
```
```
# returns
True
```

### maxDelta.py
A module for determining the greatest delta between two prime numbers in a given set. The function will return a dictionary with two elements; a list with the primes where the gap occured, and a value representing the size of the gap.

```
# finding largest delta amongst given primes
maxDelta.run(primeList)
```
```
# returns
{'primes': [887, 907], 'gap': 20}
```

### germain.py
Given a list of prime numbers, this module will return a dictionary containing all of the Germain Prime sequences identified.

```
# identifying Germain Prime sequences
germain.run(primeList)
```
```
# returns
{2: {'sequence': [2, 5, 11, 23], 'length': 4},
 3: {'sequence': [3], 'length': 1},
 5: {'sequence': [5, 11, 23], 'length': 3},
 11: {'sequence': [11, 23], 'length': 2},
 23: {'sequence': [23], 'length': 1},
 .......
```

### chebyshevFunction.py
Chebyshev's Theta Function, the log of the standard Primorial. Given a list of prime numbers and a number of values to evaluate, will return a list of each Theta(x).

```
# getting all Theta(x) through the first 100 elements in primeList
chebyshevFunction.run(primeList, 100)
```
```
# returns
[0.6931471805599453,
 1.791759469228055,
 3.401197381662155,
 5.3471075307174685,
 7.745002803515839,
 10.309952160977376,
 ........]
```

### primorial.py
The standard Primorial function. Given a list of prime numbers and a number of values to evaluate, will return a list of each P(x).

```
# getting all P(x) through the first 100 elements in primeList
primorial.run(primeList, 100)
```
```
# returns
[2,
 6,
 30,
 210,
 2310,
 30030,
 ........]
```
