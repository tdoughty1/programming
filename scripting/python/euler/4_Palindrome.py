# -*- coding: utf-8 -*-
"""
Solution to Euler problem 4:

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/problem=4

Created on Tue Apr 14 08:50:26 2015

@author: tdoughty1
"""


def Is_Palindrome(num):

    # Convert to string if it's not already
    if type(num) != str:
        num = str(num)

    # Base case: single length str, it's a palindrome
    if len(num) < 2:
        return True

    # Otherwise check if the first and last are the same, and the inner is a
    # palidrome
    else:
        return Is_Palindrome(num[1:-1]) and num[0] == num[-1]

testRange = range(100, 1000, 1)

maxPalindrome = 0
factors = (0, 0)

for i in testRange:
    for j in testRange:

        testNum = i*j
        if testNum > maxPalindrome:
            if Is_Palindrome(testNum):
                factors = (i, j)
                maxPalindrome = testNum

print maxPalindrome
