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
.. module:: eulerlib.fibonacci
    :synopsis: Functions related to Fibonacci sequence.

.. moduleauthor:: Sameer Marathe

"""

def _fibogen(start=1):
    """A generator for Fibonacci sequence.
    
    :param start: Starting digit of Fibonacci sequence (0 or 1, default=1)
    """
    if start!= 0 and  start!= 1:
        print "Assuming start = 1"
        start = 1
    if start == 0:
        f1 = 0
        f2 = 1
    elif start == 1:
        f1 = 1
        f2 = 1        
    nextf = 0
    count = 0
    while True:
        if count == 0:
            nextf = f1
        elif count == 1:
            nextf = f2
        else:
            nextf = f1 + f2
            f1 = f2
            f2 = nextf
        count += 1
        yield nextf


def first_n_fibo(n,start=1):
    """Get first *n* numbers in the Fibonacci sequence
    
    :param n: Desired length of Fibonacci sequence
    :param start: Starting digit of Fibonacci sequence (0 or 1, default=1)
    :returns: A list [f1,f2,...,fn] where f1 = 1 if start = 1
    """
    myfibo = _fibogen(start)
    result = [next(myfibo) for i in range(n)]
    return result


def fibo_less_than(n,start=1):
    """Get the Fibonacci sequence [f1,f2,...fi] such that fi < n"
    
    :param n: Desired maximum value.
    :param start: Starting digit of Fibonacci sequence (0 or 1, default=1)
    :returns: A list [f1,f2,...,fi] such that fi < n
    """
    myfibo = _fibogen(start)
    result = []
    for f in myfibo:
        if f < n:
            result.append(f)
        else:
            break
    return result


def fibo_num_digits(num,start=1):
    """Get the Fibonacci sequence [f1,f2,...fi] such that fi is the first
    Fibonacci number to have *num* digits.
    
    :param num: Desired number of digits in the last term of sequence.
    :param start: Starting digit of Fibonacci sequence (0 or 1, default=1)
    :returns: A list [f1,f2,..fi] such that fi is the first Fibonacci number
              to have *num* digits
    """
    myfibo = _fibogen(start)
    result = []
    numdigits = 0
    for f in myfibo:
        numdigits = len(str(f))
        if numdigits < num:
            result.append(f)
        elif numdigits == num:
            result.append(f)
            break
    return result
        