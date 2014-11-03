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

"""Unittests for eulerlib."""

from  unittest import TestCase
import eulerlib.numtheory as NT

class Testnumtheory(TestCase):
    def test_primes1e1(self):
        test_primes = NT.primes(10L)
        self.assertEqual(len(test_primes),4) #Number of prime
        self.assertEqual(test_primes[-1],7) #Last prime in the list
        
    def test_primes1e2(self):
        test_primes = NT.primes(100L)
        self.assertEqual(len(test_primes),25)
        self.assertEqual(test_primes[-1],97)
    
    def test_primes1e3(self):
        test_primes = NT.primes(1000L)
        self.assertEqual(len(test_primes),168)
        self.assertEqual(test_primes[-1],997)
    
    def test_primes1e4(self):
        test_primes = NT.primes(10000L)
        self.assertEqual(len(test_primes),1229)
        self.assertEqual(test_primes[-1],9973)
    
    def test_primes1e5(self):
        test_primes = NT.primes(100000L)
        self.assertEqual(len(test_primes),9592)
        self.assertEqual(test_primes[-1],99991)
    
    def test_primes1e6(self):
        test_primes = NT.primes(1000000L)
        self.assertEqual(len(test_primes),78498)
        
    def test_is_square(self):
        (is_sq,sqroot) = NT.is_square(99460729)
        self.assertTrue(is_sq)
        self.assertEqual(sqroot,9973)
    
    def test_gcd(self):
        gcd_test = NT.gcd(231675,86492)
        self.assertEqual(gcd_test,3089)
        
        

