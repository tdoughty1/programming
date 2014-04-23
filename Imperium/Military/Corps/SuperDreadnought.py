from Imperium.Military.Corps.UnitBaseClasses import Battalion, Brigade, Division
from Imperium.Military.Corps.Corps import RifleCompany, WeaponsCompany


class Battalion_Det_SD(Battalion):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RifleCompany)
        self._SubUnits.append(WeaponsCompany)


class Brigade_Det_SD(Brigade):
    pass


class Division_Det_SD(Division):
    pass
