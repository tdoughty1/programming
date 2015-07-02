# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/military/corps.py
# Description     :Classes for Marine detachments
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

from imperium.military.base_classes import Unit
from imperium.military.corps.base_unit_classes import Section, Platoon, Company, Battalion


class RifleBattalion(Battalion):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RifleCompany(self))
        self._SubUnits.append(WeaponsCompany)
        self._SubUnits.append(HSCompany_BN(self))

    def _SetPositions(self):
        self._AddPosition('Commanding Officer', 'C', 'O6', self)
        self._AddPosition('Executive Officer', 'C', 'O5', self)
        self._AddPosition('Sergeant Major', 'C', 'N5', self)


class HSCompany_BN(Company):

    def _SetSubUnits(self):
        self._SubUnits.append(ScoutSniperPlatoon_BN(self))
        self._SubUnits.append(ServicePlatoon_BN(self))
        self._SubUnits.append(MedicalPlatoon_BN(self))
        self._SubUnits.append(S1_Section_BN(self))
        self._SubUnits.append(S2_Section_BN(self))
        self._SubUnits.append(S3_Section_BN(self))
        self._SubUnits.append(S4_Section_BN(self))

    def _SetPositions(self):
        self._AddPosition('Commanding Officer', 'C', 'O3', self)
        self._AddPosition('Executive Officer', 'C', 'O2', self)
        self._AddPosition('First Sergeant', 'C', 'N4', self)
        Pos = self._SubUnits[1]._SubUnits[1]._TOE[0]
        self._AddPosition('Gunnery Sergeant', 'C', 'N3', self, pos=Pos)
        Pos = self._SubUnits[1]._SubUnits[1]._TOE[1]
        self._AddPosition('Armorer', 'C', 'N3', self, pos=Pos)


class S1_Section_BN(Section):

    def _SetPositions(self):
        self._AddPosition('Adjutant', 'C', 'O2', self)
        self._AddPosition('Personnel Officer', 'C', 'W3', self)
        self._AddPosition('Personnel Admin Chief', 'C', 'N2', self)
        self._AddPosition('Personnel Chief', 'C', 'N1', self)
        for i in range(4):
            self._AddPosition('Personnel Clerk', 'C', 'E4', self)
        for i in range(4):
            self._AddPosition('Admin Clerk', 'C', 'E4', self)
        self._AddPosition('Pay Admin Manager', 'C', 'N2', self)
        self._AddPosition('Career Planner', 'C', 'N2', self)


class S2_Section_BN(Section):

    def _SetAdminSubUnits(self):
        SniperPlatoon = self._CmdUnit._SubUnits[0]
        self._AdminSubUnits.append(SniperPlatoon)

    def _SetPositions(self):
        self._AddPosition('Intelligence Officer', 'C', 'O3', self)
        self._AddPosition('Intelligence Chief', 'C', 'N3', self)
        for i in range(4):
            self._AddPosition('Intelligence Specialist', 'C', 'E4', self)


class S3_Section_BN(Section):

    def _SetPositions(self):
        self._AddPosition('Operations Officer', 'C', 'O4', self)
        self._AddPosition('Assistant Operations Officer - Training', 'C', 'O4',
                          self)
        Pos = self._CmdUnit._SubUnits[1]._SubUnits[1]._TOE[0]
        self._AddPosition('Training Chief', 'C', 'N3', self, pos=Pos)
        self._AddPosition('Info Operations Chief', 'C', 'N2', self)
        for i in range(4):
            self._AddPosition('Info Operations Specialist', 'C', 'E4', self)


class S4_Section_BN(Section):

    def _SetAdminSubUnits(self):
        SvcPlatoon = self._CmdUnit._SubUnits[1]
        self._AdminSubUnits.append(SvcPlatoon)

    def _SetPositions(self):
        self._AddPosition('Supply Officer', 'C', 'O3', self)
        self._AddPosition('Assistant Supply Officer - Embarcation', 'C', 'O2',
                          self)
        self._AddPosition('Assistant Supply Officer - Maintenance', 'C', 'O2',
                          self)
        self._AddPositions('Supply Chief', 'C', 'N3', self)
        self._AddPosition('Logistics Chief', 'C', 'N2', self)
        self._AddPosition('Embarcation Chief', 'C', 'N1', self)
        self._AddPosition('Maintenance Management Chief', 'C', 'N2', self)
        for i in range(4):
            self._AddPositions('Supply Specialist', 'C', 'E4', self)


class ServicePlatoon_BN(Platoon):

    def _SetSubUnits(self):
        self._SubUnits.append(SupplySection_BN(self))
        self._SubUnits.append(ArmorerSection_BN(self))
        self._SubUnits.append(TransportSection_BN(self))
        self._SubUnits.append(FoodServicesSection_BN(self))


class SupplySection_BN(Section):

    def _SetPositions(self):
        self._AddPosition('Cargo Bay Chief', 'C', 'N2', self)
        self._AddPosition('Cargo Bay Assistant', 'C', 'N1', self)
        for i in range(4):
            self._AddPosition('General Warehouseman', 'C', 'E4', self)


class ArmorerSection_BN(Section):

    def _SetPositions(self):
        self._AddPosition('Small Arms Repair Chief', 'C', 'N2', self)
        self._AddPosition('Armor Repair Chief', 'C', 'N2', self)
        for i in range(3):
            self._AddPosition('Small Arms Repair Technician', 'C', 'E4', self)
        for i in range(3):
            self._AddPosition('Armor Repair Technician', 'C', 'E4', self)


class TransportSection_BN(Section):
    pass  # Add assault shuttles


class FoodServicesSection_BN(Section):

    def _SetPosition(self):
        self._AddPosition('Mess Manager', 'C', 'N2', self)
        self._AddPosition('Assistant Mess Manager', 'C', 'N1', self)
        self._AddPosition('Chief Cook', 'C' 'W2', self)
        self._AddPosition('Assistant Cook', 'C', 'W1', self)
        for i in range(12):
            self._AddPosition('Food Services Specialist', 'C', 'E4', self)


class MedicalPlatoon_BN(Platoon):

    def _SetPosition(self):
        self._AddPosition('Medical Operations Officer', 'C', 'O2', self)
        self._AddPosition('Medical Service Officer', 'C', 'O3', self)

    def _SetSubUnits(self):
        self._SubUnits.append(AidStation_BN(self))
        self._SubUnits.append(EmplacedSection_BN(self))


class AidStation_BN(Section):

    def _SetPositions(self):
        self._AddPosition('Battalion Surgeon', 'C', 'O2', self)
        self._AddPosition('Physician Assistant', 'C', 'W1', self)
        self._AddPosition('Chief Medic', 'C', 'N3', self)
        for i in range(2):
            self._AddPosition('Senior Medic', 'C', 'N2', self)
        for i in range(8):
            self._AddPosition('Medic', 'C', 'N1', self)


class EmplacedSection_BN(Section):
    pass  # Link to medics in company/platoons


class ScoutSniperPlatoon_BN(Platoon):
    pass  # Link to scout teams and sniper teams in company/platoons


class RifleCompany(Company):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RiflePlatoon(self))
        self._SubUnits.append(WeaponsSection(self))

    def _SetPositions(self):
        self._AddPosition('Commanding Officer', 'C', 'O3', self)
        self._AddPosition('Executive Officer', 'C', 'O2', self)
        self._AddPosition('First Sergeant', 'C', 'N4', self)
        self._AddPosition('Clerk', 'C', 'N1', self)
        self._AddPosition('Supply Sergeant', 'C', 'N2', self)
        self._AddPosition('Armorer', 'C', 'N2', self)
        self._AddPosition('Senior Medic', 'C', 'N2', self)


class WeaponsCompany(Platoon):

    def _SetSubUnits(self):
        self._SubUnits.append(RiflePlatoon(self))
        for i in range(3):
            self._SubUnits.append(WeaponsSection(self))

    def _SetPositions(self):
        self._AddPosition('Commanding Officer', 'C', 'O3', self)
        self._AddPosition('Executive Officer', 'C', 'O2', self)
        self._AddPosition('First Sergeant', 'C', 'N4', self)
        self._AddPosition('Clerk', 'C', 'N1', self)
        self._AddPosition('Supply Sergeant', 'C', 'N2', self)
        self._AddPosition('Armorer', 'C', 'N2', self)
        self._AddPosition('Senior Medic', 'C', 'N2', self)


class RiflePlatoon(Platoon):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RifleSquad(self))
        self._SubUnits.append(PlasmaTeam(self))

    def _SetPositions(self):
        self._AddPosition('Platoon Leader', 'C', 'O1', self)
        self._AddPosition('Platoon Sergeant', 'C', 'N3', self)


class WeaponsSection(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(SniperTeam(self))
        self._SubUnits.append(ScoutTeam(self))
        for i in range(2):
            self._SubUnits.append(PlasmaTeam(self))
            self._SubUnits.append(MissileTeam(self))
            self._SubUnits.append(MortarTeam(self))

    def _SetPositions(self):
        self._AddPosition('Section Leader', 'C', 'N2', self)


class RifleSquad(Unit):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RifleTeam(self))

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Squad Sergeant', 'C', 'N2', self, pos=Pos)
        self._AddPosition('Medic', 'C', 'N1', self)


class RifleTeam(Unit):

    def _SetPositions(self):
        Roles = ['Team', 'Ready', 'Assist', 'Fire']
        count = 0
        for role in Roles:
            if count == 0:
                self._AddPosition(role, 'C', 'N1', self)
            else:
                self._AddPosition(role, 'C', 'E4', self)
            count += 1


class MissileTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Missile Team Leader', 'C', 'N1', self)
        for i in range(2):
            self._AddPosition('Missile Team Member', 'C', 'E4', self)


class MortarTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Mortar Team Leader', 'C', 'N1', self)
        for i in range(2):
            self._AddPosition('Mortar Team Member', 'C', 'E4', self)


class PlasmaTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Plasma Team Leader', 'C', 'N1', self)
        for i in range(2):
            self._AddPosition('Plasma Team Member', 'C', 'E4', self)


class SniperTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Sniper', 'C', 'N1', self)
        self._AddPosition('Spotter', 'C', 'E4', self)


class ScoutTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Scout Team Leader', 'C', 'N2', self)
        for i in range(3):
            self._AddPosition('Scout', 'C', 'E4', self)
