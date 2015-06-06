from random import randint

from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Navy.LAC.BaseClasses import LAC_Unit
from Imperium.Military.Navy.LAC.Flight import Flight


class LogisticsTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'A', 'N1',
                          posRanks=(['N2', 'E5'], [.15, .05]))
        for i in range(4):
            self._AddPosition('Team Member', 'A', 'E2',
                              posRanks=(['E5', 'E4', 'E3', 'E1'],
                                        [.1, .15, .25, .2]))


class MagazineTeam(LogisticsTeam):
    pass


class CargoTeam(LogisticsTeam):
    pass


class MessTeam(LogisticsTeam):
    pass


class LogisticsWatch(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(self._Type(self))

    def _SetPositions(self):
        self._AddPosition('Watch Leader', 'A', 'N2',
                          posRanks=(['N3', 'N1'], [.1, .2]))


class MagazineWatch(LogisticsWatch):

    def __init__(self, cmdUnit=None):
        self._Type = MagazineTeam
        Unit.__init__(self, cmdUnit)


class CargoWatch(Unit):

    def __init__(self, cmdUnit=None):
        self._Type = CargoTeam
        Unit.__init__(self, cmdUnit)


class MessWatch(Unit):

    def __init__(self, cmdUnit=None):
        self._Type = MessTeam
        Unit.__init__(self, cmdUnit)


class Magazine(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(MagazineWatch(self))

    def _SetPositions(self):
        self._AddPosition('Magazine Chief', 'A', 'N3',
                          posRanks=(['N4', 'N2'], [.05, .2]))


class CargoBay(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(MagazineWatch(self))

    def _SetPositions(self):
        self._AddPosition('Cargo Chief', 'A', 'N3',
                          posRanks=(['N4', 'N2'], [.05, .2]))


class Mess(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(MagazineWatch(self))

    def _SetPositions(self):
        self._AddPosition('Mess Chief', 'A', 'N3',
                          posRanks=(['N4', 'N2'], [.05, .2]))


class Squadron(LAC_Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Flight(self))
        self._SubUnits.append(Magazine(self))
        self._SubUnits.append(CargoBay(self))
        self._SubUnits.append(Mess(self))

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Commanding Officer', 'A', 'O5', pos=Pos,
                          posRanks=(['O6', 'O4'], [.05, .15]))
        Pos = self._SubUnits[randint(1, 3)]._TOE[0]
        self._AddPosition('Executive Officer', 'A', 'O4', pos=Pos,
                          posRanks=(['O5', 'O3'], [.05, .2]))
        Pos = self._SubUnits[0]._TOE[1]
        self._AddPosition('Squadron Chief', 'A', 'N5', pos=Pos,
                          posRanks=(['N6', 'N4'], [.05, .15]))

    def _SetCallSign(self, cmdUnit):
        sNames = ['Red', 'Blue', 'Green', 'Gold']
        self._CallSign = sNames[len(cmdUnit._SubUnits)]

    def __repr__(self):
        return self._CallSign + ' Squadron at ' + hex(id(self))

    def __str__(self):
        return self._CallSign + ' Squadron'
