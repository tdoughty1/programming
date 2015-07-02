# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/military/core/position
# Description     :Abstract class for all military job classes
# Author          :Todd Doughty
# Date            :5 Jul 2014
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

""" imperium/military/core/position.py

    This module contains the abstract base classes from which all
    military role classes derive.

    Classes:
        Position - Base class for all military roles
"""

# File metadata
__license__ = "The MIT License (MIT)"
__copyright__ = "Copyright (c) 2015 Todd Doughty"
__version__ = "0.1"
__docformat__ = 'reStructuredText'

# Import Common Modules
from numpy import random

# Import Third Party Modules
from faker import Faker

# Import Imperium Modules
from imperium.base_classes import ImpObject
from imperium.military.structure_classes import Branched, Ranked

# Instantiate a useful factory (speeds up initalization)
fake = Faker()

class Position(ImpObject, Branched, Ranked):

    def __init__(self, name, branch=None, rank=None, unit=None,
                 pos=None, posRanks=None):
        ImpObject.__init__(self)

        self._LinkedPosition = []

        self._SetName(name)
        self._SetBranch(branch)
        self._SetRank(rank)

        if unit is not None:
            self._SetUnit(unit)

        if pos is not None:
            self._LinkPosition(pos)

        if posRanks is not None:
            self._AddPosRank(posRanks[0], posRanks[1])

    def __repr__(self):
        return '<' + self._name + ' Position at ' + hex(id(self)) + '>'

    ###################################################################
    # Set Function Checking Routines
    ###################################################################
    def _SetUnit(self, unit):
        if not isinstance(unit, Unit):
            print 'ERROR in Position():'
            print 'Unit must be a unit object!'
            exit(1)
        self._unit = unit

    ###################################################################
    # Set Function Checking Routines
    ###################################################################

    def _LinkPosition(self, oldPos):

        # First link old position to new position
        self._LinkedPosition.append(oldPos)

        # Next link all positions linked to the old position to new
        # position and link new position to all positions linked to the
        # old position
        for pos in oldPos._LinkedPosition:
            self._LinkedPosition.append(pos)
            pos._LinkedPosition.append(self)

        # Finally link this new position to the old one
        oldPos._LinkedPosition.append(self)
    
    ###################################################################
    # Public Methods
    ###################################################################
    
    def FillPosition(self):
        """Adds a randomly generated individual to this position."""
        self._Individual = {}
        self._Individual['LastName'] = fake.last_name()
        
        # Generate Random number seed
        seed = random.randint(1e9,1e10)
        gRand = seed%1000/1000.
        rRand = seed%1000000/1000/1000.
        sRand = seed%1000000000/1000000/1000.
        
        if gRand > .75:
            self._Individual['FirstName'] = fake.first_name_female()
        else:
            self._Individual['FirstName'] = fake.first_name_male()
        
        # Generate Random number for rank
        prob = 0
        for rank, add_prob in zip(self._posrank['ranks'], self._posrank['probs']):
            prob += add_prob
            if rRand <= prob:
                self._Individual['Rank'] = rank
                break
        
        # Generate Random number for seniority
        self._Individual['Seniority'] = sRand
