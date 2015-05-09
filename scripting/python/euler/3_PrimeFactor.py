# -*- coding: utf-8 -*-
"""
Solution to Euler problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

https://projecteuler.net/problem=3

Created on Tue Apr 14 07:50:17 2015

@author: tdoughty1
"""


class factor(object):

    # Class initializer
    def __init__(self):

        # Define set of prime numbers, include starter values
        self._prime = set((1, 2))

    # Define recursive function - include list of primes for speedup
    def __call__(self, num):

        # Base case (prime number), return num
        if num in self._prime:
            return set((num,))

        # Otherwise, we need to factor it
        # Largest factor with be at most floor(sqrt(num))
        i = num/2

        factors = set()

        # Check all lower factors
        while i > 2:

            # Check if it's a factor, if not continue
            if num % i:
                i += 1
                continue
            else:
                factors = factors.union(self.__call__(i))
                i += 1

        # If nothing in factors, it's prime
        if len(factors) == 0:
            self._prime.add(num)
            return set((num,))

        return factors

Factor = factor()

for i in range(61):
    print Factor(i)
