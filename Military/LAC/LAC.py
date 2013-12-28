from Imperium.Military.BaseClasses import Unit


class FlightCrew(Unit):

    def _SetPositions(self):
        self._AddPosition('Commander', 'A', 'O3')
        self._AddPosition('Tactical Officer', 'A', 'O2')
        self._AddPosition('Astrogation Officer', 'A', 'O2')
        self._AddPosition('Communications Officer', 'A', 'O2')
        self._AddPosition('Engineering Officer', 'A', 'O2')
        self._AddPosition('Crew Chief', 'A', 'N1')


class RepairTeam(Unit):

    def _SetPositions(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[5]
        self._AddPosition('Crew Chief', 'A', 'N1', pos=Pos)

        for i in range(1, 7):
            self._AddPosition('Crewman', 'A', 'E4')


class LAC(Unit):

    def __init__(self, cmdUnit=None):
        if cmdUnit is not None:
            self._SetCallSign(cmdUnit)
        else:
            self._CallSign = ''
        Unit.__init__(self, cmdUnit)

    def _SetSubUnits(self):
        self._SubUnits.append(FlightCrew(self))
        self._SubUnits.append(RepairTeam(self))

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('LAC Commander', 'A', 'O3', pos=Pos)
        Unit._SetPositions(self)

    def _SetCallSign(self, cmdUnit):
        self._CallSign = '%s %d' % (cmdUnit._CallSign,
                                    len(cmdUnit._SubUnits)+1)

    def __repr__(self):
        return '<' + self._CallSign + ' at ' + hex(id(self)) + '>'

    def __str__(self):
        return self._CallSign
