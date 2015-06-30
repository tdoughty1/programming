# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/military/corps/frigate.py
# Description     :Classes for Marine detachments on frigates
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

from imperium.military.base_classes import Unit
from corps import RiflePlatoon
from base_unit_classes import Company, Battalion, Brigade, Division


class PlatoonDet(RiflePlatoon):

    def _SetPositions(self):
		RiflePlatoon._SetPositions(self)
		self._AddPosition('Gunnery Sergeant', 'C', 'N2', self)
		self._AddPosition('Quartermaster', 'C', 'N1', self)
		self._AddPosition('Clerk', 'C', 'E4', self)


class CompanyDet_HQ_XO(Unit):
	pass


class CompanyDet_HQ_CO(Unit):
	pass


class CompanyDet_HQ(Unit):
	pass


class CompanyDet(Company):
	pass


class BattalionDet_HQ_CO(Unit):
	pass


class BattalionDet_HQ_XO(Unit):
	pass


class BattalionDet_HQ_S14(Unit):
	pass


class BattalionDet_HQ_S23(Unit):
	pass


class BattalionDet_HQ(Unit):
	pass
	

class BattalionDet(Battalion):
	pass


class BrigadeDet_HQ_XO(Unit):
	pass
	

class BrigadeDet_HQ_CO(Unit):
	pass


class BrigadeDet_HQ(Unit):
	pass


class BrigadeDet(Brigade):
	pass


class DivisionDet_HQ(Unit):
	pass


class DivisionDet(Division):
	pass
