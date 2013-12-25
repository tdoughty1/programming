from Imperium.Military.BaseClasses import Unit, Position


from Imperium.Military.LAC.Squadron import Squadron


class FlightControlTeam(Unit):

    def _SetRoster(self):
        self._Roster.append(Position('Team Leader', unit=self))
        for i in range(3):
            self._Roster.append(Position('Team Member', unit=self))


class FlightControl(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightControlTeam(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Control Officer', unit=self))
        self._Roster.append(Position('Control Chief', unit=self))
        Unit._SetRoster(self)


class Wing(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Squadron(cmdUnit=self))
        self._SubUnits.append(FlightControl(cmdUnit=self))

    def _SetRoster(self):
        self._Roster.append(Position('Commanding Officer', unit=self))
        self._Roster.append(Position('Executive Officer', unit=self))
        self._Roster.append(Position('Wing Chief', unit=self))
        Unit._SetRoster(self)
