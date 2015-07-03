# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ============================================================================
# Title           :imperium/military/corps/superdreadnought.py
# Description     :Classes for Marine detachments on superdreadnoughts
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# ============================================================================

from base_unit_classes import Battalion, Brigade, Division
from corps import RifleCompany, WeaponsCompany


class BattalionDet_SD(BattalionDet):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RifleCompany)
        self._SubUnits.append(WeaponsCompany)


class BrigadeDet_HQ_SD(Unit):
    pass


class BrigadeDet_SD(BrigadeDet):
    pass


class DivisionDet_HQ_SD(DivisionDet_HQ):
    pass


class DivisionDet_SD(DivisionDet):
    pass
