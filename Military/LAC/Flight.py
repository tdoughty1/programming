from Imperium.Military.BaseClasses import Unit, Position
from Imperium.Military.LAC.LAC import LAC


class MaintTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Team Leader', branch='A', rank='N1', unit=self))

        for i in range(1, 6):
            self._Roster.append(Position('Team Member', branch='A', rank='E4', unit=self))


class MissileTeam(MaintTeam):
    pass


class WeaponsTeam(MaintTeam):
    pass


class ImpellerTeam(MaintTeam):
    pass


class CommunicationsTeam(MaintTeam):
    pass


class EnvironmentTeam(MaintTeam):
    pass


class FusionTeam(MaintTeam):
    pass


class GraviticsTeam(MaintTeam):
    pass


class ShieldTeam(MaintTeam):
    pass


class MaintenanceCrew(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(MissileTeam(cmdUnit=self))
        self._SubUnits.append(WeaponsTeam(cmdUnit=self))
        self._SubUnits.append(CommunicationsTeam(cmdUnit=self))
        self._SubUnits.append(EnvironmentTeam(cmdUnit=self))
        self._SubUnits.append(ImpellerTeam(cmdUnit=self))
        self._SubUnits.append(FusionTeam(cmdUnit=self))
        self._SubUnits.append(GraviticsTeam(cmdUnit=self))
        self._SubUnits.append(ShieldTeam(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Maintenance Chief', branch='A', rank='N2', unit=self))
        Unit._SetRoster(self)


class FlightOpsTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Team Leader', branch='A', rank='N1', unit=self))

        for i in range(1, 5):
            self._Roster.append(Position('Team Member', branch='A', rank='E4', unit=self))


class FlightOps(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightOpsTeam(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Flight Ops Chief', branch='A', rank='N2', unit=self))
        Unit._SetRoster(self)


class HangarControl(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Hangar Control Chief', branch='A', rank='N1', unit=self))
        self._Roster.append(Position('Hangar Controller', branch='A', rank='E4', unit=self))


class Hangar(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(MaintenanceCrew(cmdUnit=self))
        self._SubUnits.append(FlightOps(cmdUnit=self))
        self._SubUnits.append(HangarControl(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Chief of the Bay', branch='A', rank='N3', unit=self))
        Unit._SetRoster(self)


class Flight(Unit):

    def __init__(self, cmdUnit=None):

        if cmdUnit is not None:
            self._SetCallSign(cmdUnit)
        Unit.__init__(self, cmdUnit=cmdUnit)

    def _SetSubUnits(self):
        for i in range(6):
            self._SubUnits.append(LAC(cmdUnit=self))
        self._SubUnits.append(Hangar(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Commanding Officer', branch='A', rank='O4', unit=self))
        self._Roster.append(Position('Executive Officer', branch='A', rank='O3', unit=self))
        self._Roster.append(Position('Flight Chief', branch='A', rank='N4', unit=self))
        Unit._SetRoster(self)

    def _SetCallSign(self, cmdUnit):
        fNames = ['Alpha', 'Beta', 'Gamma', 'Delta']
        self._CallSign = '%s %s' % (cmdUnit._CallSign,
                                    fNames[len(cmdUnit._SubUnits)])

    def __repr__(self):
        return '<' + self._CallSign + ' Flight at ' + hex(id(self)) + '>'

    def __str__(self):
        names = self._CallSign.split()
        return '%s Flight: %s Squadron' % (names[1], names[0])
