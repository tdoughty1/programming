from Imperium.Military.BaseClasses import Unit, Position


class FlightCrew(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Commander', unit=self))
        self._Roster.append(Position('Tactical Officer', unit=self))
        self._Roster.append(Position('Astrogation Officer', unit=self))
        self._Roster.append(Position('Communications Officer', unit=self))
        self._Roster.append(Position('Engineering Officer', unit=self))


class RepairTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Crew Chief', unit=self))

        for i in range(1, 7):
            self._Roster.append(Position('CrewMan', unit=self))


class LAC(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(FlightCrew(cmdUnit=self))
        self._SubUnits.append(RepairTeam(cmdUnit=self))
