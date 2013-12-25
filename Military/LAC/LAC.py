from Imperium.Military.BaseClasses import Unit, Position


class FlightCrew(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Commander', branch='A', rank='O3', unit=self))
        self._Roster.append(Position('Tactical Officer', branch='A', rank='O2', unit=self))
        self._Roster.append(Position('Astrogation Officer', branch='A', rank='O2', unit=self))
        self._Roster.append(Position('Communications Officer', branch='A', rank='O2', unit=self))
        self._Roster.append(Position('Engineering Officer', branch='A', rank='O2', unit=self))


class RepairTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Crew Chief', branch='A', rank='N1', unit=self))

        for i in range(1, 7):
            self._Roster.append(Position('Crewman', branch='A', rank='E4', unit=self))


class LAC(Unit):

    def __init__(self, cmdUnit=None):
        if cmdUnit is not None:
            self._SetCallSign(cmdUnit)
        Unit.__init__(self, cmdUnit=cmdUnit)

    def _SetSubUnits(self):
        self._SubUnits.append(FlightCrew(cmdUnit=self))
        self._SubUnits.append(RepairTeam(cmdUnit=self))

    def _SetCallSign(self, cmdUnit):
        self._CallSign = '%s %d' % (cmdUnit._CallSign,
                                    len(cmdUnit._SubUnits)+1)

    def __repr__(self):
        return '<' + self._CallSign + ' at ' + hex(id(self)) + '>'

    def __str__(self):
        return self._CallSign
