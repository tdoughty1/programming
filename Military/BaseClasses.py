from sys import exit

from Imperium.BaseClasses import DObject
from Imperium.Military.StructureClasses import Rank, Branched, Ranked


class Unit(DObject, Branched):

    def __init__(self, cmdUnit=None):
        DObject.__init__(self)

        self._CmdUnit = cmdUnit
        self._SubUnits = []

        self._TOE = []

        self._SetSubUnits()
        self._SetTOE()

    def _SetSubUnits(self):
        pass

    def _SetTOE(self):

        for unit in self._SubUnits:
            self._TOE.extend(unit._TOE)

    def __len__(self):
        return len(self._TOE)


class Position(DObject, Branched, Ranked):

    def __init__(self, name, branch=None, rank=None, unit=None):
        DObject.__init__(self)

        self._SetName(name)
        self._SetBranch(branch)
        self._SetRank(rank)
        self._roles = [(name, unit)]

        if unit is None:
            self._SetUnit(unit)

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

    ##########################################################################
    # Set Function Checking Routines
    ##########################################################################

    #FIXME Combine Rank find functionality
    def AddPosition(self, name, branch=None, rank=None, unit=None):

        if self._branch.GetCode() != branch:
            print "ERROR in Position.AddPosition:"
            print "Positions must have same branch!"
            exit(1)

        if isinstance(rank, Rank):
            if rank > self._rank:
                self._SetRank(rank)
                self._SetName(name)
            self._roles.append((name, unit))
            return

        if isinstance(rank, str):
            for rankCheck in Rank._datalist:
                if rankCheck.GetCode() == rank:
                    for branchCheck in rankCheck._branch:
                        if branchCheck.GetCode() == branch:
                            if rankCheck > self._rank:
                                self._SetRank(rankCheck)
                                self._SetName(name)
                            self._roles.append((name, unit))
                            return

        print "ERROR in Position.AddPosition:"
        print "Position must have valid rank code or object!"
