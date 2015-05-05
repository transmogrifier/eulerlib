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
    :synopsis: Miscellaneous functions.

.. moduleauthor:: Sameer Marathe

"""

from ._exceptions import EulerlibInputError

__all__ = ["decimal_to_base", "is_palindrome", "is_pandigital", "num_to_list",
           "list_to_num", "word_numerical_val", "write_number", 
           "collapse_lists"]

def decimal_to_base(num,b):
    """Converts *num* from decimal to base *b*
    
    :param num: A decimal integer
    :param b: A decimal integer value for the base. 1 < b <= 36
    :returns: String that represents decimal *num* in base *b*
    
    For example::
    
        >>> decimal_to_base(8,2)
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


def is_palindrome(num,base=10):
    """Returns *True* if decimal number *num* is a Palindrome number in *base*.
    
    :param num: Decimal number to be tested
    :param base: Base of the number system in which *num* is to be tested.
                 (Default = 10)
    :returns: *True* if *num* is palindromic in *base*
    
    For example::
    
        >>> is_palidrome(3875783) #Test in default base = 10
        >>> True
        >>> is_palidrome(9,2) # 9 in base 2 is 1001
        >>> True
    """
    str_num = str(num)
    if base != 10:
        str_num = decimal_to_base(num,base)
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
    
        >>> is_pandigital(2134, 1, 4) 
        True
    """
    if(start < 0 or stop < 0 or start >9 or stop >9):
        raise EulerlibInputError('etc','is_pandigital',
                                 'start or stop parameter value is incorrect')
    elif(stop < start):
        raise EulerlibInputError('etc','is_pandigital',
                                 'start should be smaller than stop')
    else:
        test = list(range(start,stop+1))
        nl = num_to_list(num)
        if(len(nl) != (stop-start)+1):
            return False
        else:
            nl.sort()
            if(nl == test):
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
    num = 0
    if(list_of_digits == []):
        return num
    test = range(10)
    for digit in list_of_digits:
        if(not (digit in test)):
            raise EulerlibInputError('etc','list_to_num',
                                     'Invalid member in list_of_digits')
            num = 0
            break
        num = num*10 + digit
    return num


def word_numerical_val(word):
    """Returns the sum of numerical value of each letter in the
       word based on its position in the alphabet.
    """
    import string
    num_val = 0
    lcase = string.ascii_lowercase
    test_word = word.lower()
    for char in test_word:
        if not char in lcase:
            raise EulerlibInputError('etc','word_numerical_val',
                                     'Illegal character in the word')
            num_val = 0
            break
        else:
            loc = lcase.find(char)
            if (loc != -1):
                num_val = num_val + loc + 1
            else:
                raise EulerlibInputError('etc','word_numerical_val',
                                         'Illegal character in the word')
                num_val = 0
                break
    return num_val


def write_number(num):
    """Return the written English language string representation of *num*
    
    :param num: An integer number
    
    For example::
    
        >>> write_num(132)
        >>> 'one hundred and thirty-two'
    """
    ones = ["zero","one","two","three","four","five","six","seven","eight",
            "nine"]
    teens = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen",
             "seventeen","eighteen","nineteen"]
    tens = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty",
            "ninety"]
    hundred = " hundred"
    hundred_and = " hundred and "
    thousand = " thousand"
    thousand_and = " thousand "
    minus = "minus "
    num1 = abs(num)
    number = ""
    if num1 < 1000000:
        if num1 < 10:
            number = ones[num1]
        elif num1 >= 10 and num1 < 100:
            if num1%10 == 0:
                #divisible by 10
                number = tens[(num1//10)-1]
            elif num1 > 10 and num1 < 20:
                #teens
                number = teens[num1-11]
            else:
                #create number by recursion
                tens_val = num1//10
                ones_val = num1%10
                number = tens[tens_val-1] + "-" + ones[ones_val]
        elif num1 >= 100 and num1 < 1000:
            if num1%100 == 0:
                hundreds_val = num1//100
                number = write_number(hundreds_val) + hundred
            else:
                hundreds_val = num1//100
                rest_of_num = num1%100
                number = ones[hundreds_val] + hundred_and + \
                         write_number(rest_of_num)
        else:
            thousands_val = num1//1000
            rest_of_num = num1%1000
            if rest_of_num == 0:            
                number = write_number(thousands_val) + thousand
            else:
                number = write_number(thousands_val) + thousand_and + \
                         write_number(rest_of_num)
        if num < 0:
            number = minus + number
    else:
        number = "out of range"
    return number


def collapse_lists(list1,list2,compf,pathf):
    """Function to collapse two lists into a single list based on comparison
    and path functions.
    
    :param list1: First list
    :param list2: Second list
    :param compf: Comparator function to compare values returned by
                  path function.
    :param pathf: Function that takes a list of elements and returns a
                  value of the same type.
    :returns: A list with length = len(list2)
    
    .. note::    
        * Both lists must have values of the same type 'T'
        * Comparison function should take a list of values of type 'T' and 
          return a value of type 'T'.
        * Path function should take a list of values of type 'T' and return a 
          value of type 'T'.
        * The function calculates path totals based on paths from list1 to 
          list2.
        * The difference between lengths of list1 and list2 should be 1
    
    For example: To calculate maximum sum of path values - 
    path function => sum, comparison function => max::
    
        >>> list1 = [12,37,53,46]
        >>> list2 = [23,34,47]
        >>> compf = max
        >>> pathf = sum
        >>> collapse_lists(list1,list2,compf,pathf)
        >>> [60, 87, 100]
    """
    result = []
    len1 = len(list1)
    len2 = len(list2)
    if (abs(len1-len2) != 1):
        pass
    elif(list1 == []):
        result = list(list2)
    elif(list2 == []):
        result = list(list1)
    else:
        small2large = True
        if(len1 > len2):
            small2large = False
        for j in range(len2):
            if(small2large):            
                if(j == 0):
                    val = pathf([list2[j],list1[0]])
                elif(j == len2-1):
                    val = pathf([list2[j],list1[len1-1]])
                else:
                    pv1 = pathf([list2[j],list1[j-1]])
                    pv2 = pathf([list2[j],list1[j]])
                    val = compf([pv1, pv2])
                result.append(val)
            else:
                pv1 = pathf([list2[j],list1[j+1]])
                pv2 = pathf([list2[j],list1[j]])
                val = compf([pv1, pv2])
                result.append(val)
    return result