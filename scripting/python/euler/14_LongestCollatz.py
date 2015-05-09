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

from numpy import log2, mod


def Collatz(n, debug=False):

    count = 1

    while n > 1:

        count += 1

        if debug:
            print n

        if n % 2:  # Odd numbers
            n = 3*n + 1
        elif not mod(log2(n), 1):  # Powers of 2
            power = int(log2(n)) - 1
            count += power
            if debug:
                for i in xrange(power, -1, -1):
                    print 2**i
            break
        else:    # Event numbers
            n = n/2

    return count

maxLength = 0
num = 0

testOut = Collatz(13, True)
print "Collatz Length of 13 =", testOut


for i in xrange(1, 1000001, 2):  # Longest chain will be odd

    print i
    newLength = Collatz(i)

    if newLength > maxLength:
        maxLength = newLength
        num = i

