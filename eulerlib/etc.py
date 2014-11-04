# -*- coding: utf-8 -*-
#   Copyright 2014 Sameer Suhas Marathe
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
.. module:: eulerlib.etc
    :synopsis: Miscellaneous functions.

.. moduleauthor:: Sameer Marathe

"""

def decimal_to_base(num,b):
    """Converts *num* from decimal to base *b*
    
    :param num: A decimal integer
    :param b: A decimal integer value for the base. 1 < b <= 36
    :returns: String that represents decimal *num* in base *b*
    
    For example::

        >>>decimal_to_base(8,2)
        '1000'
    """
    symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
               'q','r','s','t','u','v','w','x','y','z']
    numstring = ""
    if(b > 36 or b < 2):
        return numstring
    else:
        done = False
        while(not done):
            cur_digit = num%b
            if(cur_digit > 9):
                cur_str = symbols[cur_digit - 10]
            else:
                cur_str = str(cur_digit)
            numstring = cur_str+numstring
            num = num//b
            if(num < b):
                if(num != 0):
                    if(num > 9):
                        cur_str = symbols[num - 10]
                    else:
                        cur_str = str(num)
                    numstring = cur_str + numstring
                done = True
        return numstring


def is_palindrome(num):
    """Returns *True* if *num* is a Palindrome number"""
    str_num = str(num)
    rev_num = str_num[::-1]
    if(str_num == rev_num):
        return True
    else:
        return False


def is_pandigital(num,start,stop):
    """Returns *True* if *num* is Pandigital.
    
    :param num: An integer to be checked for pandigitalness.
    :param start: Strating digit. 0 <= start <= 9
    :param stop: Ending digit start < stop <= 9
    
    For example::
    
        >>is_pandigital(2134, 1, 4) 
        True
    """
    if(start < 0 or stop < 0 or start >9 or stop >9):
        print "Error: start or stop is invalid"
        return False
    elif(stop < start):
        print "Error: stop > start"
        return False
    else:
        test = range(start,stop+1)
        nl = num_to_list(num)
        if(len(nl) != (stop-start)+1):
            return False
        else:
            nl.sort()
            if(nl ==test):
                return True
            else:
                return False


def num_to_list(num):
    """Returns a list of digits in num (most significant digit first)."""
    result = []
    if (num < 0):
        return result
    else:
        str_num = str(num)
        for c in str_num:
            result.append(int(c))
        return result


def list_to_num(list_of_digits):
    """Returns an integer from a *list_of_digits*."""
    num = 0L
    if(list_of_digits == []):
        return num
    test = range(10)
    for digit in list_of_digits:
        if(not (digit in test)):
            print "Error: invalid members in list_of_digits"
            num = 0L
            break
        num = num*10L + digit
    return num


def word_numerical_val(word):
    """Returns the sum of numerical value of each letter in the
       word based on its position in the alphabet.
    """
    import string
    num_val = 0L
    ucase = string.ascii_uppercase
    lcase = string.ascii_lowercase
    for char in word:
        if (not char in lcase) and (not char in ucase):
            print "Error: Illegal character in the word"
            num_val = 0L
            break
        else:
            loc = ucase.find(char)
            if (loc != -1):
                num_val = num_val + loc + 1
            else:
                loc = lcase.find(char)
                if (loc !=-1):
                    num_val = num_val + loc + 1
                else:
                    print "Error: Illegal character in the word"
                    num_val = 0L
                    break
    return num_val

