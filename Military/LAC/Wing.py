from Imperium.Military.BaseClasses import Unit, Position


from Imperium.Military.LAC.Squadron import Squadron


class FlightControlTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Team Leader', branch='A', rank='N3', unit=self))
        for i in range(3):
            self._Roster.append(Position('Team Member', branch='A', rank='N1', unit=self))


class FlightControl(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightControlTeam(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Control Officer', branch='A', rank='O4', unit=self))
        self._Roster.append(Position('Control Chief', branch='A', rank='N5', unit=self))
        Unit._SetRoster(self)


class Wing(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Squadron(cmdUnit=self))
        self._SubUnits.append(FlightControl(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Commanding Officer', branch='A', rank='O6', unit=self))
        self._Roster.append(Position('Executive Officer', branch='A', rank='O5', unit=self))
        self._Roster.append(Position('Wing Chief', branch='A', rank='N6', unit=self))
        Unit._SetRoster(self)
