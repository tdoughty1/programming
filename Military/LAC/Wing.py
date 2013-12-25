from Imperium.Military.BaseClasses import Unit, Position


from Imperium.Military.LAC.Squadron import Squadron


class FlightControlTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Team Leader', 'N3', unit=self))
        for i in range(3):
            self._Roster.append(Position('Team Member', 'N1', unit=self))


class FlightControl(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightControlTeam(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Control Officer', 'O4', unit=self))
        self._Roster.append(Position('Control Chief', 'N5', unit=self))
        Unit._SetRoster(self)


class Wing(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Squadron(cmdUnit=self))
        self._SubUnits.append(FlightControl(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Commanding Officer', 'O6', unit=self))
        self._Roster.append(Position('Executive Officer', 'O5', unit=self))
        self._Roster.append(Position('Wing Chief', 'N6', unit=self))
        Unit._SetRoster(self)
