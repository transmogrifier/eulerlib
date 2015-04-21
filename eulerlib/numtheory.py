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
.. module:: eulerlib.numtheory
    :synopsis: Number theory related functions.

.. moduleauthor:: Sameer Marathe

"""

def primes(num):
    """Returns a list of prime numbers.
    
    :param num: The upper limit for prime numbers list (pn < num)
    :returns: List of prime numbers [p1,p2,...pn] such that pn < num.
    
    Uses the Sieve of Eratosthanes algorithm.
    """
    from math import sqrt as SQRT, floor as FLOOR
    from bitarray import bitarray
    maxprime = num
    result = []
    if(maxprime <=2):
        return result
    # Setup a bitarray that represents only the odd numbers from 1 to maxprime
    num_odd = maxprime//2
    domain = bitarray(num_odd)
    domain.setall(True)
    #The first element of the bitarray represents 1, set it to False to 
    # indicate it is not prime
    domain[0] = False
    # Add the only even prime to the results array.
    currprime = 2
    result.append(currprime)
    start = 0
    done = False
    root = FLOOR(SQRT(maxprime))
    while (not done):
        for index in range(start,num_odd):
            if(domain[index]):
                break
        currprime = 2*index+1
        result.append(currprime)
        if(currprime > root):
            done = True
        else:
            start = index + currprime
            if(start < num_odd-1):
                for index1 in range(start,num_odd,currprime):
                    domain[index1] = False
            elif start == num_odd-1:
                domain[start] = False
            start = index+1
    # Move the remaining primes into an array
    for i in range(index+1,num_odd):
        if(domain[i]):
            result.append(2*i+1)
    del domain
    return result


def is_square(num):
    """Determines if a positive integer *num* is the perfect square.
    
    :param num: Integer to be checked
    :returns: A tuple (is_square,root)
    
    .. note::
       
       * *is_square* is *True* if *num* is a perfect square. 
       * The integer *root* <= (square root of *num*).
    
    Uses *digit by digit* algorithm in base 10.
    """
    if(num == 0):
        pn = 0
        rn = 1
    else:
        z = num
        test = []
        while(z !=0):
            test.append(z%100)
            z = z//100
        test.reverse()
        pn = 0
        rn = 0
        for i in range(len(test)):
            #get an estimate of xn
            c = 100*rn + test[i]
            xn = 1
            while ((20*pn+xn)*xn <= c):
                xn += 1
            xn -= 1
            rn = c - (20*pn+xn)*xn
            pn = pn*10 + xn
    if(rn == 0):
        return (True,pn)
    else:
        return (False,pn)


def gcd(a,b):
    """Calculates Greatest Common Divisor of two integers.
    
    :param a: First integer
    :param b: Second integer
    :returns: Greatest Common Divisor (GCD) of *a* and *b*
    
    Uses Euclid's algorithm.
    """
    if(a==b): return a
    if(a== 0): return b
    if(b== 0): return a
    if(a==1 or b==1): return 1
    if(a>b):
        big, small = a, b
    else:
        big, small = b, a
    r = big%small
    while(r != 0):
        big = small
        small = r
        r = big%small
    return small


def lcm(a,b):
    """Calculates the Least Common Multiple (LCM) of two integers.
    
    :param a: First integer
    :param b: Second integer
    :returns: Least Common Multiple (LCM) of *a* and *b*
    """
    lcm_ab = 0L
    if a!=0 or b!=0:
        lcm_ab = abs(a*b)/gcd(a,b)
    return lcm_ab  


def lcm_n(num_list):
    """Calculate the Least Common Multiple of a list of integers.
    
    :param num_list: A list of integers *[i1,i2,i3,...,in]*
    :returns: LCM of the integers in *num_list*
    
    Uses the associative property LCM(a,b,c) = LCM(*LCM(a,b)*,c)
    """
    result = 0L
    lennum = len(num_list)
    if not (lennum <=1 or sum(num_list) == 0L):
        cindex = 1
        while cindex < lennum:
            if cindex == 1:
                curr_lcm = lcm(num_list[cindex-1],num_list[cindex])
            else:
                curr_lcm = lcm(curr_lcm,num_list[cindex])
            cindex += 1
        result = curr_lcm
    return result


def nCr(n,r):
    """Calculate ways of selecting *r* members out of a collection of *n*
    members.
    
    :param n: Size of the collection
    :param r: Number of members to be selected from the collection
    :returns: n!/[r!(n-r)!]
    
    .. note::
        
        :sup:`n` C :sub:`r` is typically read as *n combination r*. Order of 
        members is *not* important in the combination. E.g. There are :sup:`4`   
        C :sub:`2` = 6 ways of selecting two members out of a collection 
        (A, B, C, D) => AB, AC, AD, BC, BD, CD.
    """
    result = 0
    if n >= 0 and r >= 0 and r <= n:
        num = 1
        denom = 1
        for i in range(r):
            num *= (n-i)
            denom *= (i+1)
        result = num/denom
    return result


def nPr(n,r):
    """Calculate number of permutations of lengt *r* out of a collection of 
    *n* members (No repeated members).
    
    :param n: Size of the collection
    :param r: Number of members to be permutated.
    :returns: n!/[(n-r)!]
    
    .. note::
        
        :sup:`n` P :sub:`r` is typically read as *n permutation r*. Order of 
        members *is* important in the permutation. E.g. There are :sup:`4` P 
        :sub:`2` = 12 permutations of length 2 out of a collection  
        (A, B, C, D) => AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB, DC.
    """
    result = 0
    if n >= 0 and r >= 0 and r <= n:
        num = 1
        denom = 1
        for i in range(r):
            num *= (n-i)
        result = num/denom
    return result


class Divisors:
    """Implements methods related to prime factors and divisors."""
    
    def __init__(self,maxnum=1000):
        """Constructor for *Divisors* class
        
        :param maxnum: Upper limit for the list of primes. (default = 1000)
        """
        self.limit = maxnum
        self.primes_table = primes(maxnum)
        self.sigma_table = {}
        self.primefact_table = {}
        self.pfactonly_table = {}
        self.divisors_table = {}

    def sigma_function(self,num):
        """Calculates the divisor functions (sigma functions).
        
        :param num: Integer for which sigma functions are needed.
        :returns: A tuple (sigma0,sigma1,s(n))
        
        .. note::
            
            * sigma0 = number of divisors of *num*.
            * sigma1 = sum of *all* divisors of *num*
            * s(n) = sum of *proper* divisors of *num* 
              (includes 1, excludes *num*)
        
        """
        if num in self.sigma_table:
            return self.sigma_table[num]
        elif ((num < 1) or (num > self.limit)):
            return ()
        elif num == 1:
            return (1,1,0)
        elif (num in self.primes_table):
            return (2,num+1,1)
        else:
            sigma0 = 1
            sigma1 = 1
            #Implement divisor fucntion
            pfs = self.prime_factors(num)
            for (pi,ai) in pfs:
                sigma0 = sigma0*(ai+1)
                temp = 0
                for i in range(ai+1):
                    temp = temp + pi**i
                sigma1 = sigma1*temp
            result = (sigma0,sigma1,sigma1-num)
            self.sigma_table[num] = result
            return result

    def prime_factors(self,num):
        """Returns the prime factors of *num*
        
        :param num: An integer for which prime factors are needed
        :returns: A list of tuples [(pf1,a1),...(pfi,ai)]
        
       .. note::
        
            num = (pf1**a1)*(pf2**a2)..*(pfi**ai)
        """
        if num in self.primefact_table:
            return self.primefact_table[num]
        elif ((num < 2) or (num > self.limit)):
            return []
        elif num in self.primes_table:
            self.primefact_table[num] = [(num,1)]
            return [(num,1)]
        else:
            result = []
            tnum = num
            for prime in self.primes_table:
                if(tnum%prime==0):
                    ai = 2
                    pdiv = prime*prime
                    while(tnum%pdiv==0):
                        ai += 1
                        pdiv *= prime
                    ai -= 1
                    pdiv //= prime
                    result.append((prime,ai))
                    tnum //= pdiv
                    if(tnum in self.primes_table):
                        result.append((tnum,1))
                        break
                    elif(tnum==1):
                        break
            self.primefact_table[num] = result
            return result

    def prime_factors_only(self,num):
        """Returns the prime factors of *num*
        
        :param num: An integer for which prime factors are needed
        :returns: A list [pf1,pf2,...pfi] of prime factors of *num*
        """
        if num in self.pfactonly_table:
            return self.pfactonly_table[num]
        elif ((num < 2) or (num > self.limit)):
            return []
        elif num in self.primes_table:
            self.pfactonly_table[num] = [num]
            return [num]
        else:
            result = []
            tnum = num
            for prime in self.primes_table:
                if(tnum%prime==0):
                    result.append(prime)
                    pdiv = prime*prime
                    while(tnum%pdiv == 0):
                        pdiv *= prime
                    pdiv //= prime
                    tnum //= pdiv
                    if(tnum in self.primes_table):
                        result.append(tnum)
                        break
                    elif(tnum == 1):
                        break
            self.pfactonly_table[num] = result
            return result

    def divisors(self,num):
        """Returns a list of ALL divisors of *num* (including 1 and num).
        
        :param num: An integer for which divisors are needed.
        :returns: A list [d1,d2,...dn] of divisors of *num*
        """
        result = []
        if (num < 1) or (num > self.limit):
            return result
        result.append(1L)
        if (num == 1):
            return result
        elif (num in self.primes_table):
            result.append(num)
            self.divisors_table[num] = result
            return result
        else:
            pfs = self.prime_factors(num)
            for (pi,ai) in pfs:
                newdivs = []
                for i in range(ai):
                    fact = pi**(i+1)
                    for div in result:
                        newdivs.append(div*fact)
                result += newdivs
                newdivs = []
            result.sort()
            self.divisors_table[num] = result
            return result

    def phi(self,num):
        """Returns the number of totatives of *num*
        
        :param num: Integer for which number of totatives are needed.
        :returns: Number of totatives of *num*
        
        .. note::
        
            A totative of an integer *num* is any integer *i* such that,
            0 < i < n and *GCD(i,num) == 1*.
        
        Uses Euler's totient function.
        """
        if(num < 1L):
            return 0L
        if(num == 1L):
            return 1L
        if(num in self.primes_table):
            return long(num-1)
        pfs = self.prime_factors_only(num)
        prod = long(num)
        for pfi in pfs:
            prod = prod*(pfi-1)/pfi
        return prod