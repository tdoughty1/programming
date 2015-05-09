# -*- coding: utf-8 -*-
"""
Solution to Euler problem 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=10

Created on Tue Apr 14 13:12:13 2015

@author: tdoughty1
"""


def SumPrime(n):

    # Declare initial values
    prime = 2
    testNum = prime

    # Loop until we've reached n numbers
    while testNum < n:

        isPrime = True

        # Determine number to check if it's prime
        testNum += 1

        for i in xrange(2, testNum//2 + 1):

            if testNum % i == 0:
                isPrime = False
                break

        if isPrime:
            prime += testNum

    return prime

print SumPrime(2000000)
