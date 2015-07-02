# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/military/corps/lac_carrier.py
# Description     :Classes for Marine detachments on lac carriers
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

from imperium.military.corps.base_unit_classes import Company, Battalion, Brigade
from imperium.military.corps.corps import RiflePlatoon, WeaponsSection


class CompanyDet_CLAC(CompanyDet):

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


class BattalionDet_HQ_CO_CLAC(BattalionDet_HQ_CO):
    pass


class BattalionDet_HQ_XO_CLAC(BattalionDet_HQ_XO):
    pass


class BattalionDet_HQ_CLAC(BattalionDet_HQ):
    pass


class BattalionDet_CLAC(BattalionDet):
    pass


class BrigadeDet_HQ_CO_CLAC(BrigadeDet_HQ_CO):
    pass


class BrigadeDet_HQ_XO_CLAC(BrigadeDet_HQ_XO):
    pass


class BrigadeDet_HQ_S236_CLAC(BrigadeDet_HQ_S236):
    pass


class BrigadeDet_HQ_S145_CLAC(BrigadeDet_HQ_S145):
    pass


class BrigadeDet_HQ_CLAC(BrigadeDet_HQ):
    pass


class BrigadeDet_CLAC(BrigadeDet):
    pass
