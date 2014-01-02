from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Corps.BaseUnitClasses import Platoon, Company, Battalion
from Imperium.Military.Corps.Corps import RifleSquad


class LightPlatoon_Det_FG(Platoon):

    def _SetSubUnits(self):
        for i in range(2):
            self._SubUnits.append(RifleSquad(self))

    def _SetPositions(self):
        self._AddPosition('Platoon Leader', 'C', 'O2')
        self._AddPosition('Platoon Sergeant', 'C', 'N3')
        self._AddPosition('Plasma Gunner', 'C', 'E4')
        self._AddPosition('Medic', 'C', 'N1')


class Company_Det_HQ_XO_FG(Unit):

    def _SetPositions(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[0]
        self._AddPosition('Company Executive Officer', 'C', 'O2', pos=Pos)
        Pos = self._CmdUnit._SubUnits[0]._TOE[1]
        self._AddPosition('Armorer', 'C', 'N2', pos=Pos)


class Company_Det_HQ_CO_FG(Unit):

    def _SetPositions(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[0]
        self._AddPosition('Company Commander', 'C', 'O3', pos=Pos)
        Pos = self._CmdUnit._SubUnits[0]._TOE[1]
        self._AddPosition('First Sergeant', 'C', 'N4', pos=Pos)
        self._AddPosition('Clerk', 'C', 'N1')
        self._AddPosition('Supply Sergeant', 'C', 'N2')
        Pos = self._CmdUnit._SubUnits[0]._TOE[3]
        self._AddPosition('Senior Medic', 'C', 'N2', pos=Pos)


class Company_Det_HQ_FG(Unit):

    def _SetSubUnits(self):
        CoHQ = self._CmdUnit._CmdUnit._SubUnits[0]._SubUnits[6]._SubUnits[1]
        CoHQ._AdmCmdUnit = self
        self._SubUnits.append(CoHQ)
        XoHQ = self._CmdUnit._CmdUnit._SubUnits[1]._SubUnits[6]._SubUnits[1]
        XoHQ._AdmCmdUnit = self
        self._SubUnits.append(XoHQ)


class Company_Det_FG(Company):

    def _SetSubUnits(self):
        for i in range(6):
            Platoon = self._CmdUnit._SubUnits[i]._SubUnits[6]._SubUnits[0]
            self._SubUnits.append(Platoon)
            Platoon._AdmCmdUnit = self
        self._SubUnits.append(Company_Det_HQ_FG(self))


class Battalion_Det_FG(Battalion):
    pass
