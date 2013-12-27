from Imperium.Military.BaseClasses import Unit
from Imperium.Military.LAC.LAC import LAC


class MaintTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'A', 'N1')

        for i in range(1, 6):
            self._AddPosition('Team Member', 'A', 'E4')


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
        self._SubUnits.append(MissileTeam(self))
        self._SubUnits.append(WeaponsTeam(self))
        self._SubUnits.append(CommunicationsTeam(self))
        self._SubUnits.append(EnvironmentTeam(self))
        self._SubUnits.append(ImpellerTeam(self))
        self._SubUnits.append(FusionTeam(self))
        self._SubUnits.append(GraviticsTeam(self))
        self._SubUnits.append(ShieldTeam(self))

    def _SetPositions(self):
        self._AddPosition('Maintenance Chief', 'A', 'N2')


class FlightOpsTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'A', 'N1')

        for i in range(1, 5):
            self._AddPosition('Team Member', 'A', 'E4')


class FlightOps(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightOpsTeam())

    def _SetPositions(self):
        self._AddPosition('Flight Ops Chief', 'A', 'N2')


class HangarControl(Unit):

    def _SetPositions(self):
        self._AddPosition('Hangar Control Chief', 'A', 'N1')
        self._AddPosition('Hangar Controller', 'A', 'E4')


class Hangar(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(MaintenanceCrew())
        self._SubUnits.append(FlightOps())
        self._SubUnits.append(HangarControl())

    def _SetPositions(self):
        self._AddPosition('Chief of the Bay', 'A', 'N3')


class Flight(Unit):

    def __init__(self, cmdUnit=None):

        if cmdUnit is not None:
            self._SetCallSign(cmdUnit)
        Unit.__init__(self, cmdUnit=cmdUnit)

    def _SetSubUnits(self):
        for i in range(6):
            self._SubUnits.append(LAC())
        self._SubUnits.append(Hangar())

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Flight Leader', 'A', 'O4', pos=Pos)
        Pos = self._SubUnits[0]._TOE[6]
        self._AddPosition('Flight Chief', 'A', 'N4', pos=Pos)

    def _SetCallSign(self, cmdUnit):
        fNames = ['Alpha', 'Beta', 'Gamma', 'Delta']
        self._CallSign = '%s %s' % (cmdUnit._CallSign,
                                    fNames[len(cmdUnit._SubUnits)])

    def __repr__(self):
        return '<' + self._CallSign + ' Flight at ' + hex(id(self)) + '>'

    def __str__(self):
        names = self._CallSign.split()
        return '%s Flight: %s Squadron' % (names[1], names[0])
