# -*- coding: utf-8 -*-
"""
Solution to Euler problem 14:

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

https://projecteuler.net/problem=14

Created on Tue Apr 14 12:23:19 2015

@author: tdoughty1
"""


def Collatz(n):

    count = 1

    while n > 1:

        print n
        count += 1

        if n % 2:  # Odd numbers
            n = 3*n + 1
        else:    # Event numbers
            n = n/2

    return count

maxLength = 0
num = 0

for i in xrange(1000001):

    newLength = Collatz(i)

    if newLength > maxLength:
        maxLength = newLength
        num = i
