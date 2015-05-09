# -*- coding: utf-8 -*-
"""
Solution to Euler problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10,001st prime number?

https://projecteuler.net/problem=7

Created on Tue Apr 14 12:23:19 2015

@author: tdoughty1
"""


def Prime(n):

    # Declare initial values
    prime = 2
    count = 1
    testNum = prime

    # Loop until we've reached n numbers
    while count != n:

        isPrime = True

        # Determine number to check if it's prime
        testNum += 1

        for i in xrange(2, testNum//2 + 1):

            if testNum % i == 0:
                isPrime = False
                break

        if isPrime:
            prime = testNum
            count += 1

    return prime

print Prime(10001)
