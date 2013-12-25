from Imperium.Military.BaseClasses import Unit, Position
from Imperium.Military.LAC.LAC import LAC


class MaintTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Team Leader', unit=self))

        for i in range(1, 6):
            self._Roster.append(Position('Team Member', unit=self))


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


class FlightOpsTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Team Leader', unit=self))

        for i in range(1, 5):
            self._Roster.append(Position('Team Member', unit=self))


class FlightOps(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightOpsTeam(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Flight Ops Chief', unit=self))
        Unit._SetRoster(self)


class HangarControl(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Hangar Control Chief', unit=self))
        self._Roster.append(Position('Hangar Controller', unit=self))


class Hangar(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(MaintenanceCrew(cmdUnit=self))
        self._SubUnits.append(FlightOps(cmdUnit=self))
        self._SubUnits.append(HangarControl(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Chief of the Bay', unit=self))
        Unit._SetRoster(self)


class Flight(Unit):

    def _SetSubUnits(self):
        for i in range(6):
            self._SubUnits.append(LAC(cmdUnit=self))
        self._SubUnits.append(Hangar(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Commanding Officer', unit=self))
        self._Roster.append(Position('Executive Officer', unit=self))
        self._Roster.append(Position('Flight Chief', unit=self))
        Unit._SetRoster(self)
