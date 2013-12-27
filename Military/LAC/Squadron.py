from random import randint

from Imperium.Military.BaseClasses import Unit
from Imperium.Military.LAC.Flight import Flight


class LogisticsTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'A', 'N1')
        for i in range(4):
            self._AddPosition('Team Member', 'A', 'E4')


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
        self._AddPosition('Watch Leader', 'A', 'N2')


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
        self._AddPosition('Magazine Chief', 'A', 'N3')


class CargoBay(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(MagazineWatch(self))

    def _SetPositions(self):
        self._AddPosition('Cargo Chief', 'A', 'N3')


class Mess(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(MagazineWatch(self))

    def _SetPositions(self):
        self._AddPosition('Mess Chief', 'A', 'N3')


class Squadron(Unit):

    def __init__(self, cmdUnit=None):

        if cmdUnit is not None:
            self._SetCallSign(cmdUnit)
        Unit.__init__(self, cmdUnit)

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Flight())
        self._SubUnits.append(Magazine())
        self._SubUnits.append(CargoBay())
        self._SubUnits.append(Mess())

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Commanding Officer', 'A', 'O5', pos=Pos)
        Pos = self._SubUnits[randint(1, 3)]._TOE[0]
        self._AddPosition('Executive Officer', 'A', 'O4', pos=Pos)
        Pos = self._SubUnits[0]._TOE[1]
        self._AddPosition('Squadron Chief', 'A', 'N5', pos=Pos)

    def _SetCallSign(self, cmdUnit):
        sNames = ['Red', 'Blue', 'Green', 'Gold']
        self._CallSign = sNames[len(cmdUnit._SubUnits)]

    def __repr__(self):
        return '<' + self._CallSign + ' Squadron at ' + hex(id(self)) + '>'

    def __str__(self):
        return self._CallSign + ' Squadron'
