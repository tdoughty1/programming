# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/military/corps/battleship.py
# Description     :Classes for Marine detachments on battleships
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

from base_unit_classes import Company, Battalion, Brigade
from corps import RiflePlatoon, WeaponsSection


class AugmentedCompanyDet_BB(CompanyDet):

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


class BattalionDet_HQ_BB(BattalionDet_HQ):
    pass


class BattalionDet_BB(BattalionDet):
    pass


class BrigadeDet_HQ_CO_BB(BrigadeDet_HQ_CO):
    pass


class BrigadeDet_HQ_XO_BB(BrigadeDet_HQ_XO):
    pass


class BrigadeDet_HQ_BB(BrigadeDet_HQ):
    pass


class BrigadeDet_BB(BrigadeDet):
    pass
