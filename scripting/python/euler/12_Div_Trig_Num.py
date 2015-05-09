# -*- coding: utf-8 -*-
"""
Solution to Euler problem 12:

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?

https://projecteuler.net/problem=12

Created on Tue Apr 14 20:12:01 2015

@author: tdoughty1
"""


def NumTriangDivisors(n):

    divisors = 0
    count = 0
    triangnum = 0

    while count <= 1:

        print "Divisors =", divisors
        print "Count =", count
        print "Triangle =", triangnum

        # Get Triangle number
        count += 1
        triangnum += count
        print triangnum

        finished = False

        i = 2
        factors = [1, triangnum]
        count2 = 0
        while not finished and count2 <= 1:
            count2 += 1
            if not triangnum % i:
                a = i
                b = triangnum/i

                if a < b:
                    factors.append(a)
                    factors.append(b)
                    finished = True

        divisors = len(factors)

    return triangnum

print NumTriangDivisors(5)
