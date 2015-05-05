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
.. module:: eulerlib._tests.test_eulerlib
    :synopsis: Unittests for eulerlib.

.. moduleauthor:: Sameer Marathe

"""

from  unittest import TestCase
import eulerlib.numtheory as NT
import eulerlib.etc as ETC
import eulerlib.fibonacci as FIBO
import eulerlib.prime_numbers as P

class TestPrimes(TestCase):
    
    def test_primes1e1(self):
        test_primes = P.primes(10)
        self.assertEqual(len(test_primes),4) #Number of prime
        self.assertEqual(test_primes[-1],7) #Last prime in the list
        
    def test_primes1e2(self):
        test_primes = P.primes(100)
        self.assertEqual(len(test_primes),25)
        self.assertEqual(test_primes[-1],97)
    
    def test_primes1e3(self):
        test_primes = P.primes(1000)
        self.assertEqual(len(test_primes),168)
        self.assertEqual(test_primes[-1],997)
    
    def test_primes1e4(self):
        test_primes = P.primes(10000)
        self.assertEqual(len(test_primes),1229)
        self.assertEqual(test_primes[-1],9973)
    
    def test_primes1e5(self):
        test_primes = P.primes(100000)
        self.assertEqual(len(test_primes),9592)
        self.assertEqual(test_primes[-1],99991)
    
    def test_primes1e6(self):
        test_primes = P.primes(1000000)
        self.assertEqual(len(test_primes),78498)
    
    def test_primes_wgen(self):
        test_wgen = P.primes_wheel_fact(10**7)
        self.assertEqual(len(test_wgen),664579)
        self.assertEqual(test_wgen[600000-1],8960453)

class TestNumtheory(TestCase):
        
    def test_is_square(self):
        (is_sq,sqroot) = NT.is_square(99460729)
        self.assertTrue(is_sq)
        self.assertEqual(sqroot,9973)
    
    def test_gcd(self):
        gcd_test = NT.gcd(231675,86492)
        self.assertEqual(gcd_test,3089)
        
    def test_lcm(self):
        lcm_test = NT.lcm(8345,23579)
        self.assertEqual(lcm_test,196766755)
        
    def test_lcm_n(self):
        lcmn_test = NT.lcm_n([8345, 23579, 174])
        self.assertEqual(lcmn_test,34237415370)
    
    def test_nCr(self):
        nCr_test = NT.nCr(45,7)
        self.assertEqual(nCr_test,45379620)
    
    def test_nPr(self):
        nPr_test = NT.nPr(45,7)
        self.assertEqual(nPr_test,228713284800)
    
    def test_digital_sum(self):
        test_dsum = NT.digital_sum(228713284800)
        self.assertEqual(test_dsum,45)
    
    def test_digital_root(self):
        test_droot = NT.digital_root(228713284800)
        self.assertEqual(test_droot,9)
    
    def test_divisors_class(self):
        myDiv = NT.Divisors(1000000)
        pf840 = myDiv.prime_factors(840)
        self.assertEqual(len(pf840),4)
        self.assertEqual(pf840[0][1],3)
        pf14688 = myDiv.prime_factors_only(14688)
        self.assertEqual(pf14688[-1],17)
        self.assertEqual(len(pf14688),3)
        sf14688 = myDiv.sigma_function(14688)
        self.assertEqual(sf14688[0],48)
        self.assertEqual(sf14688[1],45360)
        self.assertEqual(sf14688[2],30672)
        tot60 = myDiv.phi(60)
        self.assertEqual(tot60,16)
        div14688 = myDiv.divisors(14688)
        self.assertEqual(len(div14688),sf14688[0])
        self.assertEqual(sum(div14688),sf14688[1])

class TestEtc(TestCase):
    def test_dec_to_base(self):
        hex23456 = ETC.decimal_to_base(23456,16)
        self.assertEqual(hex23456,'5ba0')
        bin23456 = ETC.decimal_to_base(23456,2)
        self.assertEqual(bin23456,'101101110100000')
        dec1000 = ETC.decimal_to_base(1000,10)
        self.assertEqual(dec1000,'1000')
    
    def test_is_pandigital(self):
        isPD521346 = ETC.is_pandigital(521346,1,6)
        self.assertTrue(isPD521346)
        
    def test_is_palindrome(self):
        self.assertTrue(ETC.is_palindrome(3452543))
        self.assertTrue(ETC.is_palindrome(23466432))
        self.assertFalse(ETC.is_palindrome(345443))
    
    def test_word_num_val(self):
        val_sameer = ETC.word_numerical_val("Sameer")
        self.assertEqual(val_sameer,61)
        
    def test_num_to_list(self):
        list230456 = ETC.num_to_list(230456)
        num230456 = ETC.list_to_num(list230456)
        self.assertEqual(num230456,230456)
        self.assertEqual(len(list230456),6)

class TestFibonacci(TestCase):
    def test_first_n_fibo(self):
        fibo20_0 = FIBO.first_n_fibo(20,0)
        self.assertEqual(fibo20_0[-1],4181)
        fibo38_1 = FIBO.first_n_fibo(38)
        self.assertEqual(fibo38_1[-1],39088169)
    
    def test_fibo_less_than(self):
        fibo1000 = FIBO.fibo_less_than(1000)
        self.assertEqual(fibo1000[-1],987)
        self.assertEqual(len(fibo1000),16)
        fibo1e6 = FIBO.fibo_less_than(1000000,0)
        self.assertEqual(fibo1e6[-1],832040)
        self.assertEqual(len(fibo1e6),31)
    
    def test_fibo_num_digits(self):
        fibo5 = FIBO.fibo_num_digits(5)
        self.assertEqual(fibo5[-1],10946)
        self.assertEqual(len(fibo5),21)
        fibo6 = FIBO.fibo_num_digits(6,0)
        self.assertEqual(fibo6[-1],121393)
        self.assertEqual(len(fibo6),27)
        
