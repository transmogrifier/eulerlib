# -*- coding: utf-8 -*-
#   Copyright 2015 Sameer Suhas Marathe
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
.. module:: eulerlib.primes
    :synopsis: Prime numbers generation functions.

.. moduleauthor:: Sameer Marathe

"""

__all__ = ["prime_gen", "prime_wheel_fact_gen", "primes", "primes_wheel_fact",
           "is_prime"]

from itertools import islice as it_islice
from itertools import count as it_count
from itertools import compress as it_compress
from itertools import cycle as it_cycle

def prime_gen():
    """A generator function that yields prime numbers using the `Sieve of
    Eratosthenes <http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>`_
    algorithm.
       
    .. note::
    
        This function is based on the erat2a function which can be found
        `here <http://stackoverflow.com/a/3796442>`_. Variable names were
        changed and comments added for clarity.
    """
    yield 2
    comp_dict = {}
    for num in it_islice(it_count(3),0,None,2):
        p = comp_dict.pop(num,None)
        if p is not None:
            # num is a composite. Get the next composite that is not already
            # in the dictionary and that has p as prime factor. Add it to
            # the dictionary. The composite number is thus "sieved" out.
            # By taking a 2*p step, we avoid checking if test is even.
            test = num + 2*p
            while test in comp_dict:
                test = test + 2*p
            comp_dict[test] = p
        else:            
            # num is a prime.
            # Add the first composite number that has 'num' as the
            # only prime factor to the composite numbers dictionary
            comp_dict[num*num] = num
            # return num
            yield num


def prime_wheel_fact_gen():
    """A generator function that yields prime numbers using the `wheel
    factorized <http://en.wikipedia.org/wiki/Wheel_factorization>`_ `Sieve of 
    Eratosthenes`_.
    
    .. note::
    
        This function is based on the erat3 function which can be found
        `here <http://stackoverflow.com/a/3796442>`_. Variable names were
        changed and comments added for clarity.
    """
    yield 2
    yield 3
    yield 5
    # The mask is used with itertools.compress method to generate prime
    # candidates after eliminating numbers using the wheel. The mask
    # contains a 1 when the corresponding number has 2,3 or 5 as a factor
    # only odd numbers are considered so the mask has only 15 values instead
    # of 30.
    wheel_mask = [0 if x%3 == 0 or x%5 == 0 else 1 for x in range(7,37,2)]
    modulos = frozenset([x%30 for x in range(31,61,2) 
                              if x%3 != 0 and x%5 != 0])
    comp_dict = {}
    for num in it_compress(it_islice(it_count(7),0,None,2), 
                        it_cycle(wheel_mask)):
        p = comp_dict.pop(num,None)
        if p is not None:
            # num is a composite. Get the next composite that is not already
            # in the dictionary, that meets the wheel criteria and that has p 
            # as prime factor. Add it to the dictionary. The composite number 
            # is thus "sieved" out.
            # By taking a 2*p step, we avoid checking if test is even.
            test = num + 2*p
            while test in comp_dict or test%30 not in modulos:
                test = test + 2*p
            comp_dict[test] = p
            # delete 'num' from comp_dict to free memory.
        else:            
            # num is a prime.
            # Add the first composite number that has 'num' as the
            # only prime factor to the composite numbers dictionary
            comp_dict[num*num] = num
            # return num
            yield num
      

def primes(num):
    """Returns a list of prime numbers. Uses the 
    :func:`eulerlib.prime_numbers.prime_gen` generator function.
    
    :param num: The upper limit for prime numbers list (pn < num)
    :returns: List of prime numbers [p1,p2,...pn] such that pn < num.
    
    Uses the prime_gen function that uses Sieve of Eratosthanes.
    """
    mypgen = prime_gen()
    result = []
    while True:
        p = next(mypgen)
        if p > num:
            break
        else:
            result.append(p)
    mypgen.close()
    return result


def primes_wheel_fact(num):
    """Returns a list of prime numbers. Uses the 
    :func:`eulerlib.prime_numbers.prime_wheel_fact_gen` generator function.
    
    :param num: The upper limit for prime numbers list (pn < num)
    :returns: List of prime numbers [p1,p2,...pn] such that pn < num.
    
    Uses the prime_wheel_fact_gen function that uses Sieve of Eratosthanes
    with wheel factorization based on the first 3 primes: 2, 3 and 5.
    """
    mypgen = prime_wheel_fact_gen()
    result = []
    while True:
        p = next(mypgen)
        if p > num:
            break
        else:
            result.append(p)
    mypgen.close()
    return result


def is_prime(num):
    """Primality checking function: returns *True* if *num* is a prime number.
    """
    result = True
    if num < 4:
        if (num != 2 and num != 3):
            result = False
    else:
        nsqrt = int(num**0.5) + 1
        mygen = prime_gen()
        for p in mygen:
            if p > nsqrt:
                break
            if num%p == 0:
                result = False
                break
        mygen.close()
    return result

