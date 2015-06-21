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
