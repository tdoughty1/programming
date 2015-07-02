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


class LightBattalionDet_DD(BattalionDet):

    def _SetSubUnits(self):
        for i in range(2):
            self._SubUnits.append(RifleCompany)
        self._SubUnits.append(WeaponsSection)


class BrigadeDet_HQ_DD(BrigadeDet_HQ):
    pass


class BrigadeDet_DD(BrigadeDet):
    pass


class DivisionDet_HQ_DD(DivisionDet_HQ):
    pass


class DivisionDet_DD(DivisionDet):
    pass
