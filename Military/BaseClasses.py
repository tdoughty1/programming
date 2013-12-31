from sys import exit

from Imperium.BaseClasses import DObject
from Imperium.Military.StructureClasses import Branched, Ranked


class Unit(DObject, Branched):

    ##########################################################################
    # Basic Magic Methods
    ##########################################################################

    def __init__(self, cmdUnit=None):
        DObject.__init__(self)

        self._CmdUnit = cmdUnit
        self._TacCmdUnit = None
        self._SubUnits = []

        self._TOE = []
        self._Roster = []
        self._Ranks = {}

        self._SetSubUnits()
        self._SetPositions()

    def __len__(self):

        tot = 0
        for unit in self._SubUnits:
            tot += len(unit)

        return len(self._TOE) + tot

    ##########################################################################
    # Initialization Methods
    ##########################################################################

    def _SetSubUnits(self):
        pass

    def _SetPositions(self):
        pass

    ##########################################################################
    # Private Methods
    ##########################################################################

    def _AddPosition(self, name, branch=None, rank=None, unit=None, pos=None):

        if unit is None:
            unit = self

        newPos = Position(name, branch, rank, unit, pos)

        self._TOE.append(newPos)
        self._Roster.append(newPos)
        self._AddRank(rank)

        # If linking to another position:
        #   1. pop previous position from subunit roster
        #   2. decrement rank value
        if pos is not None:
            try:
                ind = pos._unit._Roster.index(pos)
            except(ValueError):
                pass
            else:
                pos._unit._Roster.pop(ind)
            oldrank = pos._rank.GetCode()
            pos._unit._Ranks[oldrank] -= 1

    def _AddRank(self, rank):

        try:
            self._Ranks[rank] += 1
        except(KeyError):
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

    ##########################################################################
    # Public Methods
    ##########################################################################

    def ListTOE(self):

        for position in self._TOE:
            print position

        for unit in self._SubUnits:
            unit.ListTOE()

    def ListRoster(self):

        for position in self._Roster:
            print position

        for unit in self._SubUnits:
            unit.ListRoster()

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


class Position(DObject, Branched, Ranked):

    def __init__(self, name, branch=None, rank=None, unit=None, pos=None):
        DObject.__init__(self)

        self._LinkedPosition = []

        self._SetName(name)
        self._SetBranch(branch)
        self._SetRank(rank)

        if unit is not None:
            self._SetUnit(unit)

        if pos is not None:
            self._LinkPosition(pos)

    def __repr__(self):
        return '<' + self._name + ' Position at ' + hex(id(self)) + '>'

    ##########################################################################
    # Set Function Checking Routines
    ##########################################################################
    def _SetUnit(self, unit):

        if not isinstance(unit, Unit):
            print 'ERROR in Position():'
            print 'Unit must be a unit object!'
            exit(1)
        self._unit = unit

    ##########################################################################
    # Set Function Checking Routines
    ##########################################################################

    def _LinkPosition(self, pos):
        self._LinkedPosition.append(pos)
        pos._LinkedPosition.append(self)
