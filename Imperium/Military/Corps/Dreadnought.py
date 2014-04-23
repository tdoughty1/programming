from Imperium.Military.Corps.UnitBaseClasses import Battalion, Brigade, Division
from Imperium.Military.Corps.Corps import RifleCompany, WeaponsSection


class Light_Battalion_Det_DD(Battalion):

    def _SetSubUnits(self):
        for i in range(2):
            self._SubUnits.append(RifleCompany)
        self._SubUnits.append(WeaponsSection)


class Light_Brigade_Det_DD(Brigade):
    pass


class Light_Division_Det_DD(Division):
    pass
