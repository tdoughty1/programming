from Imperium.Military.BaseClasses import Unit, Position
from Imperium.Military.LAC.Flight import Flight


class LogisticsTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Team Leader', unit=self))
        for i in range(4):
            self._Roster.append(Position('Team Member', unit=self))


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

    def _SetRoster(self):
        self._Roster.append(Position('Watch Leader', unit=self))
        Unit._SetRoster(self)


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

    def _SetRoster(self):
        self._Roster.append(Position('Magazine Chief', unit=self))
        Unit._SetRoster(self)


class CargoBay(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(MagazineWatch(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Cargo Chief', unit=self))
        Unit._SetRoster(self)


class Mess(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(MagazineWatch(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Mess Chief', unit=self))
        Unit._SetRoster(self)


class Squadron(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Flight(cmdUnit=self))
        self._SubUnits.append(Magazine(cmdUnit=self))
        self._SubUnits.append(CargoBay(cmdUnit=self))
        self._SubUnits.append(Mess(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Commanding Officer', unit=self))
        self._Roster.append(Position('Executive Officer', unit=self))
        self._Roster.append(Position('Squadron Chief', unit=self))
        Unit._SetRoster(self)
