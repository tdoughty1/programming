# -*- coding: utf-8 -*-
"""
Solution to Euler problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

https://projecteuler.net/problem=5

Created on Tue Apr 14 09:04:33 2015

@author: tdoughty1
"""


def factor(num):

    print "Factoring", num
    factors = []

    # base case
    if num == 2:
        return [2]

    # Otherwise need more logic
    for i in range(2, num//2 + 1):
        
        print "Checking", i

        # Check if it's a factor
        if num % i:
            continue
        else:
            subfactors = factor(i)
            if len(subfactors) == 0:
                factors.append(i)
            else:
                factors += subfactors

    return factors

# Loop through each factor to see if it's a product of other factors/subfactors
#for i in factors:
print factor(12)
#for i in range(1, 21):
#    print i, factor(i)
