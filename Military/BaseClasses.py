from sys import exit
from Imperium.BaseClasses import DObject
from Imperium.Military.StructureClasses import Rank


class Unit(object):

    def __init__(self, cmdUnit=None):

        # Initialize Class Counter
        try:
            type(self)._datalist
        except(AttributeError):
            type(self)._datalist = []
            type(self)._number = 0

        self._CmdUnit = cmdUnit
        self._SubUnits = []

        self._Roster = []

        self._SetSubUnits()
        self._SetRoster()
        self._Add2Class()

    def _SetSubUnits(self):
        pass

    def _SetRoster(self):

        for unit in self._SubUnits:
            self._Roster.extend(unit._Roster)

    def _Add2Class(self):
        type(self)._datalist.append(self)
        type(self)._number += 1

    def __len__(self):
        return len(self._Roster)


class Position(DObject):

    def __init__(self, name, rank, unit=None):

        self._SetName(name)
        self._SetRank(rank)

        if unit is None:
            self._SetUnit(unit)

    def __repr__(self):
        return self._position + ' at ' + hex(id(self))

    ##########################################################################
    # Set Function Checking Routines
    ##########################################################################
    def _SetUnit(self, unit):

        if not isinstance(unit, Unit):
            print 'ERROR in Position():'
            print 'Unit must be a unit object!'
            exit(1)

        self._unit = unit

    def _SetRank(self, rank):

        if isinstance(rank, Rank):
            self._rank = rank
        elif isinstance(rank, str):

            isfound = False
            for rankCheck in Rank._datalist:

                if rank == rankCheck.GetCode():
                    isfound = True
                    self._rank = rank
                    break

            if not isfound:
                print 'ERROR in Position():'
                print 'Rank must be a valid rank code!'
                exit(1)

        else:
            print 'ERROR in Position():'
            print 'Rank must be a rank object or rank code!'
            exit(1)
