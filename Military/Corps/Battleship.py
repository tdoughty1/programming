from Imperium.Military.Corps.UnitBaseClasses import Company, Battalion, Brigade
from Imperium.Military.Corps.Corps import RiflePlatoon, WeaponsSection


class AugmentedCompany_Det_BB(Company):

    def _SetSubUnits(self):
        for i in range(4):
            self._SubUnits.append(RiflePlatoon(self))
        for i in range(2):
            self._SubUnits.append(WeaponsSection(self))

    def _SetPositions(self):
        self._AddPosition('Commanding Officer', 'C', 'O4')
        self._AddPosition('Executive Officer', 'C', 'O2')
        self._AddPosition('First Sergeant', 'C', 'N4')
        self._AddPosition('Clerk', 'C', 'N1')
        self._AddPosition('Supply Sergeant', 'C', 'N2')
        self._AddPosition('Armorer', 'C', 'N2')
        self._AddPosition('Senior Medic', 'C', 'N2')


class HeavyBattalion_Det_BB(Battalion):
    pass


class HeavyBrigade_Det_BB(Brigade):
    pass
