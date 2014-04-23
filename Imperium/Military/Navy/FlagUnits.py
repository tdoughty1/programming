from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Corps.Frigate import Company_Det_FG, Battalion_Det_FG
from Imperium.Military.Corps.Destroyer import Company_Det_DS, Battalion_Det_DS
from Imperium.Military.Navy.Frigate import Frigate
from Imperium.Military.Navy.Ships import Destroyer, LightCruiser, \
    HeavyCruiser, Battlecruiser, Battleship, Dreadnought, SuperDreadnought, \
    LACCarrier


class Element_FG(Unit):

    def _SetSubUnits(self):
        for i in range(6):
            self._SubUnits.append(Frigate(self))
        self._AdminUnits = [Company_Det_FG(self)]

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Element Senior Officer', 'A', 'O5', self,
                          pos=Pos)


class Flotilla_FG(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            tempElement = Element_FG(self)
            tempElement._CmdUnit = None
            tempElement._AdmCmdUnit = self
            self._SubUnits.append(tempElement)
        self._AdminUnits = [Battalion_Det_FG(self)]

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Flotilla Senior Officer', 'A', 'O6', self, pos=Pos)


class Element_DS(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Destroyer(self))
        self._AdminUnits = [Company_Det_DS(self)]

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Element Senior Officer', 'A', 'O5', self,
                          pos=Pos)


class Flotilla_DS(Unit):

    def _SetSubUnits(self):
        for i in range(4):
            tempElement = Element_DS(self)
            tempElement._CmdUnit = None
            tempElement._AdmCmdUnit = self
            self._SubUnits.append(tempElement)
        self._AdminUnits = [Battalion_Det_FG(self)]

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Flotilla Senior Officer', 'A', 'O6', self, pos=Pos)


class Element_CL(Unit):

    CO = 'Captain JG'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(LightCruiser(self))


class Flotilla_CL(Unit):

    CO = 'Captain SG'

    def _SetSubUnits(self):
        for i in range(6):
            self._SubUnits.append(Element_CL(self))


class Element_CA(Unit):

    CO = 'Captain SG'  # Not Flag

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(HeavyCruiser(self))


class Division_CA(Unit):

    CO = 'Commodore'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Element_CA(self))


class Division_BC(Unit):

    CO = 'Commodore'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Battlecruiser(self))


class Squadron_BC(Unit):

    CO = 'Rear Admiral of the Red'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Division_BC(self))


class Division_BB(Unit):

    CO = 'Commodore'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Battleship(self))


class Squadron_BB(Unit):

    CO = 'Rear Admiral of the Red'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Division_BB(self))


class Division_DD(Unit):

    CO = 'Commodore'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Dreadnought(self))


class Squadron_DD(Unit):

    CO = 'Rear Admiral of the Green'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Division_DD(self))


class Division_SD(Unit):

    CO = 'Commodore'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(SuperDreadnought(self))


class Squadron_SD(Unit):

    CO = 'Vice Admiral of the Red'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Division_SD(self))


class Division_CLAC(Unit):

    CO = 'Commodore'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(LACCarrier(self))


class Squadron_CLAC(Unit):

    CO = 'Rear Admiral of the Green'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Division_CLAC(self))
