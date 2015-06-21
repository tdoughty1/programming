# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/military/corps/dreadnought.py
# Description     :Classes for Marine detachments on dreadnoughts
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

from imperium.military.corps.base_unit_classes import Battalion, Brigade, Division
from imperium.military.corps.corps import RifleCompany, WeaponsSection


class Light_Battalion_Det_DD(Battalion):

    def _SetSubUnits(self):
        for i in range(2):
            self._SubUnits.append(RifleCompany)
        self._SubUnits.append(WeaponsSection)


class Light_Brigade_Det_DD(Brigade):
    pass


class Light_Division_Det_DD(Division):
    pass
