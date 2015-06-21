from Imperium.Military.Corps.BaseUnitClasses import Company, Battalion, Brigade
from Imperium.Military.Corps.Corps import RiflePlatoon, WeaponsSection


class Company_Det_CLAC(Company):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RiflePlatoon(self))
        self._SubUnits.append(WeaponsSection(self))

    def _SetPositions(self):
        self._AddPosition('Commanding Officer', 'C', 'O4')
        self._AddPosition('Executive Officer', 'C', 'O2')
        self._AddPosition('First Sergeant', 'C', 'N4')
        self._AddPosition('Clerk', 'C', 'N1')
        self._AddPosition('Supply Sergeant', 'C', 'N2')
        self._AddPosition('Armorer', 'C', 'N2')
        self._AddPosition('Senior Medic', 'C', 'N2')


class Battalion_Det_CLAC(Battalion):
    pass


class Brigade_Det_CLAC(Brigade):
    pass
