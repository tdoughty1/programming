# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/military/corps/superdreadnought.py
# Description     :Classes for Marine detachments on superdreadnoughts
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

from imperium.military.corps.base_unit_classes import Battalion, Brigade, Division
from imperium.military.corps.corps import RifleCompany, WeaponsCompany


class Battalion_Det_SD(Battalion):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RifleCompany)
        self._SubUnits.append(WeaponsCompany)


class Brigade_Det_SD(Brigade):
    pass


class Division_Det_SD(Division):
    pass
