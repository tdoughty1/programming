# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/military/corps/light_cruiser.py
# Description     :Classes for Marine detachments on light cruisers
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

from imperium.military.base_classes import Unit
from imperium.military.corps.detach_classes import PlatoonDet
from imperium.military.corps.base_unit_classes import Platoon, Company, Battalion
from imperium.military.corps.corps import RifleSquad, WeaponsSection


class AugmentedPlatoonDet_CL(PlatoonDet):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RifleSquad(self))
        self._SubUnits.append(WeaponsSection(self))

'''
class CompanyDet_HQ_CO_CL(CompanyDet_HQ_CO):

    def _SetPositions(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[0]
        self._AddPosition('Company Commander', 'C', 'O3', pos=Pos)
        Pos = self._CmdUnit._SubUnits[0]._TOE[1]
        self._AddPosition('First Sergeant', 'C', 'N4', pos=Pos)
        self._AddPosition('Clerk', 'C', 'N1')
        self._AddPosition('Supply Sergeant', 'C', 'N2')
        Pos = self._CmdUnit._SubUnits[0]._TOE[3]
        self._AddPosition('Senior Medic', 'C', 'N2', pos=Pos)


class CompanyDet_HQ_XO_CL(CompanyDet_HQ_XO):

    def _SetPositions(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[0]
        self._AddPosition('Company Executive Officer', 'C', 'O2', pos=Pos)
        Pos = self._CmdUnit._SubUnits[0]._TOE[2]
        self._AddPosition('Armorer', 'C', 'N2', pos=Pos)


class CompanyDet_HQ_CL(CompanyDet_HQ):

    def _SetSubUnits(self):
        CoHQ = self._CmdUnit._CmdUnit._SubUnits[0]._SubUnits[6]._SubUnits[1]
        CoHQ._AdmCmdUnit = self
        self._SubUnits.append(CoHQ)
        XoHQ = self._CmdUnit._CmdUnit._SubUnits[1]._SubUnits[6]._SubUnits[1]
        XoHQ._AdmCmdUnit = self
        self._SubUnits.append(XoHQ)


class CompanyDet_CL(CompanyDet):

    def _SetSubUnits(self):
        for i in range(4):
            Platoon = self._CmdUnit._SubUnits[i]._SubUnits[6]._SubUnits[0]
            self._SubUnits.append(Platoon)
            Platoon._AdmCmdUnit = self
        self._SubUnits.append(CompanyDet_HQ_CL(self))


class BattalionDet_HQ_CO_CL(BattalionDet_HQ_CO):
    pass


class BattalionDet_HQ_XO_CL(BattalionDet_HQ_XO):
    pass


class BattalionDet_HQ_S14_CL(BattalionDet_HQ_S14):
    pass
    
    
class BattalionDet_HQ_S23_CL(BattalionDet_HQ_S23):
    pass


class BattalionDet_HQ_CL(Battalion_HQ_CL):
    pass


class BattalionDet_CL(BattalionDet):
    pass
'''
