# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ============================================================================
# Title           :imperium/military/corps/heavycruiser.py
# Description     :Classes for Marine detachments on heavy cruisers
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# ============================================================================
from base_unit_classes import Company, Battalion, Brigade
from imperium.military.corps.corps import RiflePlatoon, WeaponsSection


class LightCompanyDet_CA(CompanyDet):

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


class BattalionDet_HQ_CO_CA(BattalionDet_HQ_CO):
    pass


class BattalionDet_HQ_XO_CA(BattalionDet_HQ_XO):
    pass


class BattalionDet_CA(BattalionDet):
    pass


class BrigadeDet_HQ_CO_CA(BrigadeDet_HQ_CO):
    pass


class BrigadeDet_HQ_XO_CA(BrigadeDet_HQ_XO):
    pass


class BrigadeDet_HQ_S145_CA(BrigadeDet_HQ_S145):
    pass


class BrigadeDet_HQ_S136_CA(BrigadeDet_HQ_S136):
    pass


class BrigadeDet_HQ_CA(BrigadeDet_HQ):
    pass


class BrigadeDet_CA(BrigadeDet):
    pass
