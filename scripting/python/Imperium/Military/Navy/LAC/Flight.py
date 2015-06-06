from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Navy.LAC.BaseClasses import LAC_Unit
from Imperium.Military.Navy.LAC.LAC import LAC


class MaintTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'A', 'N1', posRanks=(['N2','E5'],[.2,.05]))

        for i in range(1, 6):
            self._AddPosition('Team Member', 'A', 'E2', posRanks=(['E5','E4','E3','E1'], [.1,.15,.25,.2]))


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
        self._AddPosition('Maintenance Chief', 'A', 'N2', posRanks=(['N3','N1'],[.1,.15]))


class FlightOpsTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'A', 'N1', posRanks=(['N2','E5'],[.2,.05]))

        for i in range(1, 5):
            self._AddPosition('Team Member', 'A', 'E2', posRanks=(['E5','E4','E3','E1'], [.1,.15,.25,.2]))


class FlightOps(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightOpsTeam(self))

    def _SetPositions(self):
        self._AddPosition('Flight Ops Chief', 'A', 'N2', posRanks=(['N3','N1'],[.15,.05]))


class HangarControl(Unit):

    def _SetPositions(self):
        self._AddPosition('Hangar Control Chief', 'A', 'N1', posRanks=(['N2','E5'],[.15,.05]))
        for i in range(4):
            self._AddPosition('Hangar Controller', 'A', 'E2', posRanks=(['E5','E4','E3','E1'], [.1,.15,.25,.2]))


class Hangar(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(MaintenanceCrew(self))
        self._SubUnits.append(FlightOps(self))
        self._SubUnits.append(HangarControl(self))

    def _SetPositions(self):
        self._AddPosition('Chief of the Bay', 'A', 'N3', posRanks=(['N4','N2'], [.05,.15]))


class Flight(LAC_Unit):

    def _SetSubUnits(self):
        for i in range(6):
            self._SubUnits.append(LAC(self))
        self._SubUnits.append(Hangar(self))

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Flight Leader', 'A', 'O4', pos=Pos, posRanks=(['O5','O3'], [.05,.2]))
        Pos = self._SubUnits[0]._SubUnits[1]._TOE[0]
        self._AddPosition('Flight Chief', 'A', 'N3', pos=Pos, posRanks=(['N4','N2'], [.05,.2]))

    def _SetCallSign(self, cmdUnit):
        fNames = ['Alpha', 'Beta', 'Gamma', 'Delta']
        self._CallSign = '%s %s' % (cmdUnit._CallSign,
                                    fNames[len(cmdUnit._SubUnits)])

    def __repr__(self):
        return '<' + self._CallSign + ' Flight at ' + hex(id(self)) + '>'

    def __str__(self):
        names = self._CallSign.split()
        return '%s Flight: %s Squadron' % (names[1], names[0])
