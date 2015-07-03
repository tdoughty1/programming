# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ============================================================================
# Title           :imperium/military/corps/destroyer.py
# Description     :Classes for Marine detachments on destroyers
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# ============================================================================

from imperium.military.base_classes import Unit
from detach_classes import PlatoonDet, CompanyDet_HQ_CO, CompanyDet_HQ_XO
from detach_classes import CompanyDet_HQ, CompanyDet, BattalionDet_HQ_CO
from detach_classes import BattalionDet_HQ_XO
from base_unit_classes import Platoon, Company, Battalion
from corps import RifleSquad


class PlatoonDet_DS(PlatoonDet):
    pass

'''
class CompanyDet_HQ_CO_DS(CompanyDet_HQ_CO):

    def _SetPositions(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[0]
        self._AddPosition('Company Commander', 'C', 'O3', pos=Pos)
        Pos = self._CmdUnit._SubUnits[0]._TOE[1]
        self._AddPosition('First Sergeant', 'C', 'N4', pos=Pos)
        self._AddPosition('Clerk', 'C', 'N1')
        self._AddPosition('Supply Sergeant', 'C', 'N2')
        Pos = self._CmdUnit._SubUnits[0]._TOE[3]
        self._AddPosition('Senior Medic', 'C', 'N2', pos=Pos)


class CompanyDet_HQ_XO_DS(CompanyDet_HQ_XO):

    def _SetPositions(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[0]
        self._AddPosition('Company Executive Officer', 'C', 'O2', pos=Pos)
        Pos = self._CmdUnit._SubUnits[0]._TOE[1]
        self._AddPosition('Armorer', 'C', 'N2', pos=Pos)


class CompanyDet_HQ_DS(CompanyDet_HQ):

    def _SetSubUnits(self):
        CoHQ = self._CmdUnit._CmdUnit._SubUnits[0]._SubUnits[6]._SubUnits[1]
        CoHQ._AdmCmdUnit = self
        self._SubUnits.append(CoHQ)
        XoHQ = self._CmdUnit._CmdUnit._SubUnits[1]._SubUnits[6]._SubUnits[1]
        XoHQ._AdmCmdUnit = self
        self._SubUnits.append(XoHQ)


class CompanyDet_DS(CompanyDet):

    def _SetSubUnits(self):
        for i in range(4):
            Platoon = self._CmdUnit._SubUnits[i]._SubUnits[6]._SubUnits[0]
            self._SubUnits.append(Platoon)
            Platoon._AdmCmdUnit = self
        self._SubUnits.append(Company_Det_HQ_DS(self))


class BattalionDet_HQ_CO_DS(BattalionDet_HQ_CO):

    def _SetPositions(self):
        Flot = self._CmdUnit._CmdUnit._CmdUnit
        CO = Flot._SubUnits[0]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[0]
        self._AddPosition('Battalion Commanding Officer', 'C', 'O5', self,
                          pos=CO)
        SM = Flot._SubUnits[0]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[1]
        self._AddPosition('Sergeant Major', 'C', 'N5', self, pos=SM)
        CM = Flot._SubUnits[0]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[2]
        self._AddPosition('Battalion Chief Medic', 'C', 'N3', pos=CM)


class BattalionDet_HQ_XO_DS(BattalionDet_HQ_XO):

    def _SetPositions(self):
        Flot = self._CmdUnit._CmdUnit._CmdUnit
        CO = Flot._SubUnits[1]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[0]
        self._AddPosition('Battalion Executive Officer', 'C', 'O4', self,
                          pos=CO)


class BattalionDet_HQ_S14_DS(BattalionDet_HQ_S14):

    def _SetPositions(self):
        Flot = self._CmdUnit._CmdUnit._CmdUnit
        AS = Flot._SubUnits[3]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[0]
        self._AddPosition('Battalion Adjutant/Supply Officer', 'C', 'O3', self,
                          pos=AS)
        BQ = Flot._SubUnits[3]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[3]
        self._AddPosition('Battalion Quartermaster', 'C', 'N3', self, pos=BQ)
        BC = Flot._SubUnits[3]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[4]
        self._AddPosition('Battalion Clerk', 'C', 'N3', pos=BC)


class BattalionDet_HQ_S23_DS(BattalionDet_HQ_S23):

    def _SetPositions(self):
        Flot = self._CmdUnit._CmdUnit._CmdUnit
        OI = Flot._SubUnits[2]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[0]
        self._AddPosition('Battalion Intelligence/Operations Officer', 'C',
                          'O4', self, pos=OI)
        OC = Flot._SubUnits[2]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[1]
        self._AddPosition('Battalion Operations Chief', 'C', 'N3', self,
                          pos=OC)
        IC = Flot._SubUnits[2]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[2]
        self._AddPosition('Battalion Intelligence Chief', 'C', 'N2', self,
                          pos=IC)


class BattalionDet_HQ_DS(BattalionDet_HQ):

    def _SetSubUnits(self):
        self._SubUnits.append(Battalion_Det_HQ_CO_DS(self))
        self._SubUnits.append(Battalion_Det_HQ_XO_DS(self))
        self._SubUnits.append(Battalion_Det_HQ_S23_DS(self))
        self._SubUnits.append(Battalion_Det_HQ_S14_DS(self))


class BattalionDet_DS(BattalionDet):

    def _SetSubUnits(self):
        for i in range(4):
            Company = self._CmdUnit._SubUnits[i]._AdminUnits[0]
            self._SubUnits.append(Company)
            Company._AdmCmdUnit = self
        self._SubUnits.append(Battalion_Det_HQ_DS(self))
'''
