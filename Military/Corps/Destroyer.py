from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Corps.UnitBaseClasses import Platoon, Company, Battalion
from Imperium.Military.Corps.Corps import RifleSquad


class Platoon_Det_DS(Platoon):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RifleSquad(self))

    def _SetPositions(self):
        self._AddPosition('Platoon Leader', 'C', 'O2')
        self._AddPosition('Platoon Sergeant', 'C', 'N3')
        self._AddPosition('Plasma Gunner', 'C', 'E4')
        self._AddPosition('Plasma Gunner', 'C', 'E4')
        self._AddPosition('Medic', 'C', 'N1')


class Company_Det_HQ_XO_DS(Unit):

    def _SetPositions(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[0]
        self._AddPosition('Company Executive Officer', 'C', 'O2', pos=Pos)
        Pos = self._CmdUnit._SubUnits[0]._TOE[1]
        self._AddPosition('Armorer', 'C', 'N2', pos=Pos)


class Company_Det_HQ_CO_DS(Unit):

    def _SetPositions(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[0]
        self._AddPosition('Company Commander', 'C', 'O3', pos=Pos)
        Pos = self._CmdUnit._SubUnits[0]._TOE[1]
        self._AddPosition('First Sergeant', 'C', 'N4', pos=Pos)
        self._AddPosition('Clerk', 'C', 'N1')
        self._AddPosition('Supply Sergeant', 'C', 'N2')
        Pos = self._CmdUnit._SubUnits[0]._TOE[3]
        self._AddPosition('Senior Medic', 'C', 'N2', pos=Pos)


class Company_Det_HQ_DS(Unit):

    def _SetSubUnits(self):
        CoHQ = self._CmdUnit._CmdUnit._SubUnits[0]._SubUnits[6]._SubUnits[1]
        CoHQ._AdmCmdUnit = self
        self._SubUnits.append(CoHQ)
        XoHQ = self._CmdUnit._CmdUnit._SubUnits[1]._SubUnits[6]._SubUnits[1]
        XoHQ._AdmCmdUnit = self
        self._SubUnits.append(XoHQ)


class Company_Det_DS(Company):

    def _SetSubUnits(self):
        for i in range(4):
            Platoon = self._CmdUnit._SubUnits[i]._SubUnits[6]._SubUnits[0]
            self._SubUnits.append(Platoon)
            Platoon._AdmCmdUnit = self
        self._SubUnits.append(Company_Det_HQ_DS(self))


class Battalion_Det_DS(Battalion):
    pass
