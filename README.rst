EulerLib
********

*Eulerlib* is a library of recreational mathematics and number theory related 
functions inspired by  `Project Euler`_. Available 
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
*eulerlib* is avalaible through Python Package Index (`PyPI`_) using `pip`_. ::

   >>> pip install --upgrade eulerlib

To uninstall using `pip`_. ::

   >>> pip uninstall eulerlib

Usage
-----
In Python console you can import functions/classes from eulerlib as needed. ::

   >>> from eulerlib import primes
   >>> p10 = primes(10)
   >>> print p10
   [2, 3, 5, 7]

The *Divisors* class implements functions related to prime factorization,
sigma functions etc. ::

   >>> from eulerlib import Divisors
   >>> mydiv = Divisors(10000)
   >>> div84 = mydiv.divisors(84) #divisors of 84
   >>> print div84
   [1L, 2L, 3L, 4L, 6L, 7L, 12L, 14L, 21L, 28L, 42L, 84L]
   >>> pf840 = mydiv.prime_factors(840) #prime factors of 840
   >>> print pf840
   [(2, 3), (3, 1), (5, 1), (7, 1)]

**Example**: Solved `Project Euler`_ `problem 3`_. ::

    from eulerlib import is_square, primes
    #get approximate square root of number since
    #largest prime factor < sq. root
    (is_sq, sqroot) = is_square(600851475143L)
    #get a list of primes less than the approx. square root.
    test_primes = primes(sqroot + 1L)
    #test the primes from the list to find the largest factor
    len_p = len(test_primes)
    for i in range(1,len_p+1):
        j = 0 - i
        test_fact = test_primes[j]
        if 600851475143L%test_fact == 0:
            break
    answer = test_fact #Set the answer

See complete `documentation`_.

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

Development
-----------
Source code repositories (`GitHub`_, `BitBucket`_) are available. 
`Bug reports`_ and suggestions are most welcome.

License
-------
eulerlib is licensed under `Apache License 2.0`_.

.. _Project Euler: https://projecteuler.net
.. _PyPI: https://pypi.python.org/pypi
.. _pip: https://pip.pypa.io
.. _Apache License 2.0: https://www.apache.org/licenses/LICENSE-2.0.html
.. _problem 3: https://projecteuler.net/problem=3
.. _GitHub: https://github.com/transmogrifier/eulerlib
.. _BitBucket: https://bitbucket.org/transmogrifier/eulerlib
.. _Bug reports: https://github.com/transmogrifier/eulerlib/issues
.. _documentation: http://pythonhosted.org/eulerlib