# -*- coding: utf-8 -*-
"""
Solution to Euler problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1

Created on Mon Apr 13 07:19:50 2015

@author: tdoughty1
"""

# Initialize sum
total = 0

i = 1000

while i > 0:
    i -= 1

    if not (i % 3 and i % 5):
        total += i

print(total)
