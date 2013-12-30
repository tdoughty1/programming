from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Corps.Frigate import Company_Det_FG
from Imperium.Military.Navy.Frigate import Frigate
from Imperium.Military.Navy.Ships import Destroyer, LightCruiser, \
    HeavyCruiser, Battlecruiser, Battleship, Dreadnought, SuperDreadnought, \
    LACCarrier


class Element_FG(Unit):

    CO = 'Commander'

    def _SetSubUnits(self):
        for i in range(6):
            self._SubUnits.append(Frigate(self))
        self._SubUnits.append(Company_Det_FG(self))


class Flotilla_FG(Unit):

    CO = 'Captain JG'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Element_FG(self))


class Element_DS(Unit):

    CO = 'Commander'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Destroyer(self))


class Flotilla_DS(Unit):

    CO = 'Captain JG'

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(Flotilla_DS(self))


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
