from random import sample

from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Navy.LAC.Squadron import Squadron


class FlightControlTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'A', 'N3', posRanks=(['N4','N2'],[.05,.15]))
        for i in range(3):
            self._AddPosition('Team Member', 'A', 'N1', posRanks=(['N2','E5'],[.15,.05]))


class FlightControl(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(FlightControlTeam(self))

    def _SetPositions(self):
        self._AddPosition('Control Officer', 'A', 'O4', posRanks=(['O5','O3'],[.05,.2]))
        self._AddPosition('Control Chief', 'A', 'N5', posRanks=(['N6','N4'],[.05,.15]))


class Wing(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Squadron(self))
        self._SubUnits.append(FlightControl(self))

    def _SetPositions(self):
        rands = sample(range(4), 2)
        Pos = self._SubUnits[rands[0]]._TOE[0]
        self._AddPosition('Commanding Officer', 'A', 'O6', pos=Pos, posRanks=(['O6+','O5'],[.05,.2]))
        Pos = self._SubUnits[rands[1]]._TOE[0]
        self._AddPosition('Executive Officer', 'A', 'O5', pos=Pos, posRanks=('O4',.2))
        Pos = self._SubUnits[rands[0]]._TOE[2]
        self._AddPosition('Wing Chief', 'A', 'N6', pos=Pos, posRanks=('N5',.2))
