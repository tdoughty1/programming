# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:30:02 2013

@author: tdoughty1
"""

from UnionFind import UnionFind


def main():
    f = open('tinyUF.txt', 'r')

    f.readline()  # Ignore Comment

    N = f.readline()  # Get Number of elements
    uf = UnionFind(int(N))

    lines = f.readlines()
    for line in lines:
        p = line.split()[0]
        q = line.split()[1]

        if not uf.connected(p, q):
            uf.union(p, q)
            print '%d %d' % (p, q)

if __name__ == '__main__':

    main()
