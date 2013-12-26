from random import randint

from Imperium.Military.BaseClasses import Unit, Position
from Imperium.Military.LAC.Flight import Flight


class LogisticsTeam(Unit):

    def _SetTOE(self):
        self._TOE.append(Position('Team Leader', 'A', 'N1', unit=self))
        for i in range(4):
            self._TOE.append(Position('Team Member', 'A', 'E4', unit=self))


class MagazineTeam(LogisticsTeam):
    pass


class CargoTeam(LogisticsTeam):
    pass


class MessTeam(LogisticsTeam):
    pass


class LogisticsWatch(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(self._Type(cmdUnit=self))

    def _SetTOE(self):
        self._TOE.append(Position('Watch Leader', 'A', 'N2', unit=self))
        Unit._SetTOE(self)


class MagazineWatch(LogisticsWatch):

    def __init__(self, cmdUnit=None):
        self._Type = MagazineTeam
        Unit.__init__(self, cmdUnit=cmdUnit)


class CargoWatch(Unit):

    def __init__(self, cmdUnit=None):
        self._Type = CargoTeam
        Unit.__init__(self, cmdUnit=cmdUnit)


class MessWatch(Unit):

    def __init__(self, cmdUnit=None):
        self._Type = MessTeam
        Unit.__init__(self, cmdUnit=cmdUnit)


class Magazine(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(MagazineWatch(cmdUnit=self))

    def _SetTOE(self):
        self._TOE.append(Position('Magazine Chief', 'A', 'N3', unit=self))
        Unit._SetTOE(self)


class CargoBay(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(MagazineWatch(cmdUnit=self))

    def _SetTOE(self):
        self._TOE.append(Position('Cargo Chief', 'A', 'N3', unit=self))
        Unit._SetTOE(self)


class Mess(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(MagazineWatch(cmdUnit=self))

    def _SetTOE(self):
        self._TOE.append(Position('Mess Chief', 'A', 'N3', unit=self))
        Unit._SetTOE(self)


class Squadron(Unit):

    def __init__(self, cmdUnit=None):

        if cmdUnit is not None:
            self._SetCallSign(cmdUnit)
        Unit.__init__(self, cmdUnit=cmdUnit)

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Flight(cmdUnit=self))
        self._SubUnits.append(Magazine(cmdUnit=self))
        self._SubUnits.append(CargoBay(cmdUnit=self))
        self._SubUnits.append(Mess(cmdUnit=self))

    def _SetTOE(self):
        Pos = self._SubUnits[0]._TOE[0]
        Pos.AddPosition('Commanding Officer', 'A', 'O5', unit=self)
        self._TOE.append(Pos)
        Pos = self._SubUnits[randint(1, 3)]._TOE[0]
        Pos.AddPosition('Executive Officer', 'A', 'O4', unit=self)
        self._TOE.append(Pos)
        Pos = self._SubUnits[0]._TOE[1]
        Pos.AddPosition('Squadron Chief', 'A', 'N5', unit=self)
        self._TOE.append(Pos)
        Unit._SetTOE(self)

    def _SetCallSign(self, cmdUnit):
        sNames = ['Red', 'Blue', 'Green', 'Gold']
        self._CallSign = sNames[len(cmdUnit._SubUnits)]

    def __repr__(self):
        return '<' + self._CallSign + ' Squadron at ' + hex(id(self)) + '>'

    def __str__(self):
        return self._CallSign + ' Squadron'
