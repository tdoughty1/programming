from random import sample

from Imperium.Military.BaseClasses import Unit, Position
from Imperium.Military.LAC.Squadron import Squadron


class FlightControlTeam(Unit):

    def _SetTOE(self):
        self._TOE.append(Position('Team Leader', 'A', 'N3', unit=self))
        for i in range(3):
            self._TOE.append(Position('Team Member', 'A', 'N1', unit=self))


class FlightControl(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightControlTeam(cmdUnit=self))

    def _SetTOE(self):
        self._TOE.append(Position('Control Officer', 'A', 'O4', unit=self))
        self._TOE.append(Position('Control Chief', 'A', 'N5', unit=self))
        Unit._SetTOE(self)


class Wing(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Squadron(cmdUnit=self))
        self._SubUnits.append(FlightControl(cmdUnit=self))

    def _SetTOE(self):
        rands = sample(range(4), 2)
        Pos = self._SubUnits[rands[0]]._TOE[0]
        Pos.AddPosition('Commanding Officer', 'A', 'O6', unit=self)
        self._TOE.append(Pos)
        Pos = self._SubUnits[rands[1]]._TOE[0]
        Pos.AddPosition('Executive Officer', 'A', 'O5', unit=self)
        self._TOE.append(Pos)
        Pos = self._SubUnits[rands[0]]._TOE[2]
        Pos.AddPosition('Wing Chief', 'A', 'N6', unit=self)
        self._TOE.append(Pos)
        Unit._SetTOE(self)
