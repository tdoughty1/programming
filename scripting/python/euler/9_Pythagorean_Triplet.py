# -*- coding: utf-8 -*-
"""
Solution to Euler problem 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://projecteuler.net/problem=9

Created on Tue Apr 14 12:47:11 2015

@author: tdoughty1
"""

from numpy import sqrt


def PythagoreanTriplet(n):

    for b in range(1, n//2):
        for a in range(1, b):

            # Get valid c
            c = sqrt(a**2 + b**2)

            # It has to be an integer
            if int(c) == c:
                c = int(c)
            else:
                continue

            # Check that it adds to 1000
            if a + b + c == n:
                return(a, b, c, a*b*c)

print PythagoreanTriplet(1000)
