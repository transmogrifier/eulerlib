========
EulerLib
========
*Eulerlib* is a library of recreational mathematics and number theory related 
functions inspired by  `Project Euler <https://projecteuler.net/>`_. Available 
functions include:

* Prime number generation
* Divisor functions (sigma functions)
* Euler's totient function
* Greatest Common Divisor (GCD) using Euclid's algorithm
* Integer square root
* Fibonacci numbers
* Pandigital numbers
* Palindrome numbers
* Pythagorean triples

Functions from this library can be used to solve recreational mathematics and
programming problems such as problems in Project Euler.

Installation
------------
*eulerlib* is avalaible through Python Package Index (`PyPI 
<https://pypi.python.org/pypi>`_) using `pip 
<http://www.pip-installer.org/en/latest/index.html>`_.::

   >>> pip install --upgrade eulerlib

To uninstall using `pip
<http://www.pip-installer.org/en/latest/index.html>`_.::

   >>> pip uninstall eulerlib

Usage
-----
In Python console you can import functions/classes from eulerlib as needed::

   >>> from eulerlib import primes
   >>> p10 = primes(10)
   >>> print p10
   [2, 3, 5, 7]

The *Divisors* class implements functions related to prime factorization,
sigma functions etc.::

   >>> from eulerlib import Divisors
   >>> mydiv = Divisors(10000)
   >>> div84 = mydiv.divisors(84) #divisors of 84
   >>> print div84
   [1L, 2L, 3L, 4L, 6L, 7L, 12L, 14L, 21L, 28L, 42L, 84L]
   >>> pf840 = mydiv.prime_factors(840) #prime factors of 840
   >>> print pf840
   [(2, 3), (3, 1), (5, 1), (7, 1)]

See :ref:`reference` for detailed documentation of all the functions in the 
library. See an example solved Project Euler problem.

Modules
-------
+--------------+--------------------------------------------------------------+
|numtheory.py  | * Function to generate lists of primes.                      |
|              | * Euler's divisor functions (sigma funtions)                 |
|              | * Euler's totient function (phi function)                    |
|              | * Greatest Common Divisor (GCD)                              |
+--------------+--------------------------------------------------------------+
|fibonacci.py  | Functions related to the Fibonacci sequence.                 |
+--------------+--------------------------------------------------------------+
|pythagoras.py | Functions related to Pythagorean triples.                    |
+--------------+--------------------------------------------------------------+
|etc.py        | Miscellaneous functions:                                     |
|              |                                                              |
|              | * Pandigital numbers                                         |
|              | * Conversion from decimal to base n (2-36)                   |
|              | * Number to lists and vice versa                             |
|              | * Palindrome numbers                                         |
+--------------+--------------------------------------------------------------+

License
-------
eulerlib is licensed under `Apache License 2.0 
<https://www.apache.org/licenses/LICENSE-2.0.html>`_.
