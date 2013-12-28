from random import sample

from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Navy.LAC.Squadron import Squadron


class FlightControlTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'A', 'N3')
        for i in range(3):
            self._AddPosition('Team Member', 'A', 'N1')


class FlightControl(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightControlTeam(self))

    def _SetPositions(self):
        self._AddPosition('Control Officer', 'A', 'O4')
        self._AddPosition('Control Chief', 'A', 'N5')


class Wing(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Squadron(self))
        self._SubUnits.append(FlightControl(self))

    def _SetPositions(self):
        rands = sample(range(4), 2)
        Pos = self._SubUnits[rands[0]]._TOE[0]
        self._AddPosition('Commanding Officer', 'A', 'O6', pos=Pos)
        Pos = self._SubUnits[rands[1]]._TOE[0]
        self._AddPosition('Executive Officer', 'A', 'O5', pos=Pos)
        Pos = self._SubUnits[rands[0]]._TOE[2]
        self._AddPosition('Wing Chief', 'A', 'N6', pos=Pos)
