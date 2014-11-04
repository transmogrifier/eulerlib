========
EulerLib
========
A library of number theory related functions inspired by 
`Project Euler <https://projecteuler.net/>`_. Available functions include:

* Prime number generation
* Divisor functions (sigma functions)
* Euler's totient function
* Greatest Common Divisor (GCD) using Euclid's algorithm
* Integer square root
* Fibonacci numbers
* Pandigital numbers
* Palindrome numbers
* Pythagorean triples

Functions from this library can be used to solve problems in Project Euler.

Installation
------------
*eulerlib* is avalaible through Python Package Index ('PyPI 
<https://pypi.python.org/pypi>`_) using `pip 
<http://www.pip-installer.org/en/latest/index.html>`_.::

   $ pip install --upgrade eulerlib

To uninstall using `pip
<http://www.pip-installer.org/en/latest/index.html>`_.::

   $ pip uninstall eulerlib

Usage
-----

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
