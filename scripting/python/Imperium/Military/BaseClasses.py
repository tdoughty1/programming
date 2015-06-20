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

    This module contains the abstract base classes from which most
    other military classes are derived from.

    Classes:
        Unit - Base class for all miltary units.
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
from Imperium.BaseClasses import ImpObject
from Imperium.Military.StructureClasses import Branched, Ranked

# Instantiate a useful factory (speeds up initalization)
fake = Faker()

class Unit(ImpObject, Branched):
    """The "abstract" base class for all military units

    All military units inherit most of their basic functionality
    through this class.
    
    - **parameters**, **types**, **return** and **return types**::

          :param arg1: description
          :param arg2: description
          :type arg1: type description
          :type arg1: type description
          :return: return description
          :rtype: the return type description

    - and to provide sections such as **Example** using the double commas syntax::

          :Example:

          followed by a blank line !

      which appears as follow:

      :Example:

      followed by a blank line

    - Finally special sections such as **See Also**, **Warnings**, **Notes**
      use the sphinx syntax (*paragraph directives*)::

          .. seealso:: blabla
          .. warnings also:: blabla
          .. note:: blabla
          .. todo:: blabla

    .. note::
        There are many other Info fields but they may be redundant:
            * param, parameter, arg, argument, key, keyword: Description of a
              parameter.
            * type: Type of a parameter.
            * raises, raise, except, exception: That (and when) a specific
              exception is raised.
            * var, ivar, cvar: Description of a variable.
            * returns, return: Description of the return value.
            * rtype: Return type.

    .. note::
        There are many other directives such as versionadded, versionchanged,
        rubric, centered, ... See the sphinx documentation for more details.

    Here below is the results of the :func:`function1` docstring.

    """
    ###################################################################
    # Basic Magic Methods
    ###################################################################

    def __init__(self, cmdUnit=None):
        """
        Initializer for all Unit objects.

        All unit objects call this function directly (can't be overloa

          - parameters using ``:param <name>: <description>``
          - type of the parameters ``:type <name>: <description>``
          - returns using ``:returns: <description>``
          - examples (doctest)
          - seealso using ``.. seealso:: text``
          - notes using ``.. note:: text``
          - warning using ``.. warning:: text``
          - todo ``.. todo:: text``

        **Advantages**:
         - Uses sphinx markups, which will certainly be improved in future
           version
         - Nice HTML output with the See Also, Note, Warnings directives


        **Drawbacks**:
         - Just looking at the docstring, the parameter, type and  return
           sections do not appear nicely

        :param arg1: the first value
        :param arg2: the first value
        :param arg3: the first value
        :type arg1: int, float,...
        :type arg2: int, float,...
        :type arg3: int, float,...
        :returns: arg1/arg2 +arg3
        :rtype: int, float

        :Example:

        >>> import template
        >>> a = template.MainClass1()
        >>> a.function1(1,1,1)
        2

        .. note:: can be useful to emphasize
            important feature
        .. seealso:: :class:`MainClass2`
        .. warning:: arg2 must be non-zero.
        .. todo:: check that arg2 is non zero.
        """

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
