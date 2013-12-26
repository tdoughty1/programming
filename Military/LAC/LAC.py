from Imperium.Military.BaseClasses import Unit, Position


class FlightCrew(Unit):

    def _SetTOE(self):
        self._TOE.append(Position('Commander', 'A', 'O3', unit=self))
        self._TOE.append(Position('Tactical Officer', 'A', 'O2', unit=self))
        self._TOE.append(Position('Astrogation Officer', 'A', 'O2', unit=self))
        self._TOE.append(Position('Communications Officer', 'A', 'O2', unit=self))
        self._TOE.append(Position('Engineering Officer', 'A', 'O2', unit=self))
        self._TOE.append(Position('Crew Chief', 'A', 'N1', unit=self))


class RepairTeam(Unit):

    def _SetTOE(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[5]
        Pos.AddPosition('Crew Chief', 'A', 'N1', unit=self)
        self._TOE.append(Pos)

        for i in range(1, 7):
            self._TOE.append(Position('Crewman', 'A', 'E4', unit=self))


class LAC(Unit):

    def __init__(self, cmdUnit=None):
        if cmdUnit is not None:
            self._SetCallSign(cmdUnit)
        Unit.__init__(self, cmdUnit=cmdUnit)

    def _SetSubUnits(self):
        self._SubUnits.append(FlightCrew(cmdUnit=self))
        self._SubUnits.append(RepairTeam(cmdUnit=self))

    def _SetTOE(self):
        Pos = self._SubUnits[0]._TOE[0]
        Pos.AddPosition('LAC Commander', 'A', 'O3', unit=self)
        self._TOE.append(Pos)
        Unit._SetTOE(self)

    def _SetCallSign(self, cmdUnit):
        self._CallSign = '%s %d' % (cmdUnit._CallSign,
                                    len(cmdUnit._SubUnits)+1)

    def __repr__(self):
        return '<' + self._CallSign + ' at ' + hex(id(self)) + '>'

    def __str__(self):
        return self._CallSign
