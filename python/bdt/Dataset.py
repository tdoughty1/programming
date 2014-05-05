# -*- coding: utf-8 -*-
"""
Created on Mon May  5 14:02:44 2014

@author: tdoughty1
"""

# Create a dataset similar to Bernards drawings:

import numpy as np


def Create_Dataset():

    #Signal
    xS = np.arange(0, 1, 1e-3)
    yS = np.sqrt(1-xS**2) + .15 - .3*np.random.rand(len(xS))
    xS = xS + .15 - .3*np.random.rand(len(xS))
    nS = len(xS)

    # Background
    xB1 = 2*np.random.rand(len(xS)/8)
    yB1 = 2*np.random.rand(len(yS)/8)
    nB1 = len(xB1) + nS

    theta = np.pi/2*np.random.rand(2*len(xS)/8)
    xB2 = .8*np.random.rand(2*len(xS)/8)*np.cos(theta)
    yB2 = .8*np.random.rand(2*len(xS)/8)*np.sin(theta)
    nB2 = len(xB2) + nB1

    theta = np.pi/2*np.random.rand(3*len(xS)/8)
    xB3 = (1.2 + .5*np.random.rand(3*len(xS)/8))*np.cos(theta)
    yB3 = (1.2 + .5*np.random.rand(3*len(xS)/8))*np.sin(theta)
    nB3 = len(xB3) + nB2

    xB4 = (.8 + .75*np.random.rand(2*len(xS)/8))
    yB4 = (.8 + .75*np.random.rand(2*len(xS)/8))
    nB4 = len(xB4) + nB3

    # Initialize Data Array
    Dataset = np.zeros([2000, 3])

    # Add Data into array

    # Start with Signal
    Dataset[0:nS, 0] = xS
    Dataset[0:nS, 1] = yS
    Dataset[0:nS, 2] = 1

    # Then Backgrounds
    Dataset[nS:nB1, 0] = xB1
    Dataset[nS:nB1, 1] = yB1
    Dataset[nS:nB1, 2] = 0

    Dataset[nB1:nB2, 0] = xB2
    Dataset[nB1:nB2, 1] = yB2
    Dataset[nB1:nB2, 2] = 0

    Dataset[nB2:nB3, 0] = xB3
    Dataset[nB2:nB3, 1] = yB3
    Dataset[nB2:nB3, 2] = 0

    Dataset[nB3:nB4, 0] = xB4
    Dataset[nB3:nB4, 1] = yB4
    Dataset[nB3:nB4, 2] = 0

    np.random.shuffle(Dataset)

    return Dataset

test = Create_Dataset()