# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :Imperium/Military/BaseClasses.py
# Description     :Set of basic classes for inheritance
# Author          :Todd Doughty
# Date            :5 Jul 2014
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

""" Imperium/Military/BaseClasses.py

    Module containing the base class from which most other classes are
    derived from.

    Classes:
        ImpObject - Base class for most Imperium classes.
"""

from numpy import random

from faker import Faker

from Imperium.BaseClasses import ImpObject
from Imperium.Military.StructureClasses import Branched, Ranked


class Unit(ImpObject, Branched):

    ###################################################################
    # Basic Magic Methods
    ###################################################################

    def __init__(self, cmdUnit=None):
        ImpObject.__init__(self)

        self._CmdUnit = cmdUnit
        self._AdmCmdUnit = None
        self._SubUnits = []

        self._TOE = []
        self._CTOE = []
        self._Ranks = {}

        self._SetSubUnits()
        self._SetPositions()

    def __len__(self):

        tot = 0
        for unit in self._SubUnits:
            tot += len(unit)

        return len(self._TOE) + tot

    ###################################################################
    # Initialization Methods
    ###################################################################

    def _SetSubUnits(self):
        pass

    def _SetPositions(self):
        pass

    ###################################################################
    # Private Methods
    ###################################################################

    def _AddPosition(self, name, branch=None, rank=None, unit=None,
                     pos=None, posRanks=None):

        if unit is None:
            unit = self

        newPos = Position(name, branch, rank, unit, pos, posRanks)

        self._TOE.append(newPos)
        self._CTOE.append(newPos)
        self._AddRank(rank)

        # If linking to another position:
        #   1. pop previous position from subunit roster
        #   2. decrement rank value
        if pos is not None:
            try:
                ind = pos._unit._CTOE.index(pos)
            except ValueError:
                pass
            else:
                pos._unit._CTOE.pop(ind)
            oldrank = pos._rank.GetCode()
            pos._unit._Ranks[oldrank] -= 1

    def _AddRank(self, rank):

        try:
            self._Ranks[rank] += 1
        except KeyError:
            self._Ranks[rank] = 1

    def _GetAllRanks(self):

        tempRankDict = {}
        tempRankDict.update(self._Ranks)

        for unit in self._SubUnits:
            tempDict = unit._GetAllRanks()
            for key in tempDict:
                if key in tempRankDict:
                    tempRankDict[key] += tempDict[key]
                else:
                    tempRankDict[key] = tempDict[key]

        return tempRankDict

    ###################################################################
    # Public Methods
    ###################################################################

    def ListTOE(self):

        for position in self._TOE:
            print position

        for unit in self._SubUnits:
            unit.ListTOE()

    def ListCTOE(self):

        for position in self._CTOE:
            print position

        for unit in self._SubUnits:
            unit.ListCTOE()

    def ListBaseRanks(self):

        keys = self._Ranks.keys()
        keys.sort()

        for key in reversed(keys):
            print '%s: %d' % (key, self._Ranks[key])

    def ListRanks(self):
        tempDict = self._GetAllRanks()
        keys = tempDict.keys()
        keys.sort()

        for key in reversed(keys):
            print '%s: %d' % (key, tempDict[key])
            
    def ListRoster(self):
        
        for position in self._CTOE:
            print position._Individual['FirstName'], \
                  position._Individual['LastName'], \
                  str(position._Individual['Rank'])
        
        for unit in self._SubUnits:
            unit.ListRoster()

    def FillPositions(self):
        
        for position in self._CTOE:
            position.FillPosition()
        
        for unit in self._SubUnits:
            unit.FillPositions()

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
        fake = Faker()
        self._Individual = {}
        self._Individual['LastName'] = fake.last_name()
        
        # Generate Random number for gender
        gRand = random.rand()
        if gRand > .75:
            self._Individual['FirstName'] = fake.first_name_female()
        else:
            self._Individual['FirstName'] = fake.first_name_male()
        
        # Generate Random number for rank
        rRand = random.rand()
        prob = 0
        for rank, add_prob in zip(self._posrank['ranks'], self._posrank['probs']):
            prob += add_prob
            if rRand <= prob:
                self._Individual['Rank'] = rank
                break
        
        # Generate Random number for seniority
        sRand = random.rand()
        self._Individual['Seniority'] = sRand
