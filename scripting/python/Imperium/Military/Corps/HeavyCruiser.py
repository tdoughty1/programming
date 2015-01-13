from Imperium.Military.Corps.UnitBaseClasses import Company, Battalion, Brigade
from Imperium.Military.Corps.Corps import RiflePlatoon, WeaponsSection


class LightCompany_Det_CA(Company):

    def _SetSubUnits(self):
        for i in range(2):
            self._SubUnits.append(RiflePlatoon(self))
        self._SubUnits.append(WeaponsSection(self))

    def _SetPositions(self):
        self._AddPosition('Commanding Officer', 'C', 'O3')
        self._AddPosition('Executive Officer', 'C', 'O2')
        self._AddPosition('First Sergeant', 'C', 'N4')
        self._AddPosition('Clerk', 'C', 'N1')
        self._AddPosition('Supply Sergeant', 'C', 'N2')
        self._AddPosition('Armorer', 'C', 'N2')
        self._AddPosition('Senior Medic', 'C', 'N2')


class LightBattalion_Det_CA(Battalion):
    pass


class LightBrigade_Det_CA(Brigade):
    pass
