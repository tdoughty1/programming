from Imperium.Military.BaseClasses import Unit, Position


class FlightCrew(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Commander', 'O3', unit=self))
        self._Roster.append(Position('Tactical Officer', 'O2', unit=self))
        self._Roster.append(Position('Astrogation Officer', 'O2', unit=self))
        self._Roster.append(Position('Communications Officer', 'O2', unit=self))
        self._Roster.append(Position('Engineering Officer', 'O2', unit=self))


class RepairTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Crew Chief', unit=self))

        for i in range(1, 7):
            self._Roster.append(Position('Crewman' + str(i), unit=self))


class LAC(Unit):

    def __init__(self, cmdUnit=None):
        if cmdUnit is not None:
            self._CallSign = '%s %d' % (cmdUnit._CallSign,
                                        len(cmdUnit._SubUnits)+1)
        Unit.__init__(self, cmdUnit=cmdUnit)

    def _SetSubUnits(self):
        self._SubUnits.append(FlightCrew(cmdUnit=self))
        self._SubUnits.append(RepairTeam(cmdUnit=self))

    def __repr__(self):
        return '<' + self._CallSign + ' at ' + hex(id(self)) + '>'

    def __str__(self):
        return self._CallSign
