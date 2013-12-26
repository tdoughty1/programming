from Imperium.Military.BaseClasses import Unit, Position
from Imperium.Military.LAC.LAC import LAC


class MaintTeam(Unit):

    def _SetTOE(self):
        self._TOE.append(Position('Team Leader', 'A', 'N1', unit=self))

        for i in range(1, 6):
            self._TOE.append(Position('Team Member', 'A', 'E4', unit=self))


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

    def _SetTOE(self):
        self._TOE.append(Position('Maintenance Chief', 'A', 'N2', unit=self))
        Unit._SetTOE(self)


class FlightOpsTeam(Unit):

    def _SetTOE(self):
        self._TOE.append(Position('Team Leader', 'A', 'N1', unit=self))

        for i in range(1, 5):
            self._TOE.append(Position('Team Member', 'A', 'E4', unit=self))


class FlightOps(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightOpsTeam(cmdUnit=self))

    def _SetTOE(self):
        self._TOE.append(Position('Flight Ops Chief', 'A', 'N2', unit=self))
        Unit._SetTOE(self)


class HangarControl(Unit):

    def _SetTOE(self):
        self._TOE.append(Position('Hangar Control Chief', 'A', 'N1', unit=self))
        self._TOE.append(Position('Hangar Controller', 'A', 'E4', unit=self))


class Hangar(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(MaintenanceCrew(cmdUnit=self))
        self._SubUnits.append(FlightOps(cmdUnit=self))
        self._SubUnits.append(HangarControl(cmdUnit=self))

    def _SetTOE(self):
        self._TOE.append(Position('Chief of the Bay', 'A', 'N3', unit=self))
        Unit._SetTOE(self)


class Flight(Unit):

    def __init__(self, cmdUnit=None):

        if cmdUnit is not None:
            self._SetCallSign(cmdUnit)
        Unit.__init__(self, cmdUnit=cmdUnit)

    def _SetSubUnits(self):
        for i in range(6):
            self._SubUnits.append(LAC(cmdUnit=self))
        self._SubUnits.append(Hangar(cmdUnit=self))

    def _SetTOE(self):
        Pos = self._SubUnits[0]._TOE[0]
        Pos.AddPosition('Flight Leader', 'A', 'O4', unit=self)
        self._TOE.append(Pos)
        Pos = self._SubUnits[0]._TOE[6]
        Pos.AddPosition('Flight Chief', 'A', 'N4', unit=self)
        self._TOE.append(Pos)
        Unit._SetTOE(self)

    def _SetCallSign(self, cmdUnit):
        fNames = ['Alpha', 'Beta', 'Gamma', 'Delta']
        self._CallSign = '%s %s' % (cmdUnit._CallSign,
                                    fNames[len(cmdUnit._SubUnits)])

    def __repr__(self):
        return '<' + self._CallSign + ' Flight at ' + hex(id(self)) + '>'

    def __str__(self):
        names = self._CallSign.split()
        return '%s Flight: %s Squadron' % (names[1], names[0])
