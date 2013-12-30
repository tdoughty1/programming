from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Corps.BaseUnitClasses import Platoon, Company


class RifleCompany(Company):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RiflePlatoon(self))
        self._SubUnits.append(WeaponsPlatoon(self))

    def _SetPositions(self):

        self._AddPosition('Commanding Officer', 'C', 'O3')
        self._AddPosition('Executive Officer', 'C', 'O2')
        self._AddPosition('First Sergeant', 'C', 'N4')
        self._AddPosition('Clerk', 'C', 'N1')
        self._AddPosition('Supply Sergeant', 'C', 'N2')
        self._AddPosition('Armorer', 'C', 'N2')
        self._AddPosition('Senior Medic', 'C', 'N2')


class WeaponsPlatoon(Platoon):

    def _SetSubUnits(self):
        self._SubUnits.append(RiflePlatoon(self))
        for i in range(2):
            self._SubUnits.append(WeaponsPlatoon(self))

    def _SetPositions(self):
        self._AddPosition('Platoon Leader', 'C', 'O1')
        self._AddPosition('Platoon Sergeant', 'C', 'N3')
        self._AddPosition('Plasma Gunner', 'C', 'E4')
        self._AddPosition('Plasma Gunner', 'C', 'E4')
        self._AddPosition('Medic', 'C', 'N1')


class RiflePlatoon(Platoon):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RifleSquad(self))
        self._SubUnits.append(WeaponsSection(self))

    def _SetPositions(self):
        self._AddPosition('Platoon Leader', 'C', 'O1')
        self._AddPosition('Platoon Sergeant', 'C', 'N3')
        self._AddPosition('Plasma Gunner', 'C', 'E4')
        self._AddPosition('Plasma Gunner', 'C', 'E4')
        self._AddPosition('Medic', 'C', 'N1')


class WeaponsSection(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(SniperTeam(self))
        self._SubUnits.append(ScoutTeam(self))
        for i in range(2):
            self._SubUnits.append(MissileTeam(self))
            self._SubUnits.append(MortarTeam(self))
            self._SubUnits.append(PlasmaTeam(self))

    def _SetPositions(self):
        self._AddPosition('Section Leader', 'C', 'N2')
        self._AddPosition('Medic', 'C', 'N1')


class RifleSquad(Unit):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(RifleTeam(self))

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Squad Sergeant', 'C', 'N2', pos=Pos)
        self._AddPosition('Medic', 'C', 'N1')


class RifleTeam(Unit):

    def _SetPositions(self):
        Roles = ['Team', 'Ready', 'Assist', 'Fire']
        count = 0
        for role in Roles:
            if count == 0:
                self._AddPosition(role, 'C', 'N1')
            else:
                self._AddPosition(role, 'C', 'E4')

            count += 1


class MissileTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'C', 'N1')
        for i in range(3):
            self._AddPosition('Team Member', 'C', 'E4')


class MortarTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'C', 'N1')
        for i in range(3):
            self._AddPosition('Team Member', 'C', 'E4')


class PlasmaTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'C', 'N1')
        for i in range(3):
            self._AddPosition('Team Member', 'C', 'E4')


class SniperTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Sniper', 'C', 'N1')
        self._AddPosition('Spotter', 'C', 'E4')


class ScoutTeam(Unit):

    def _SetPositions(self):
        self._AddPosition('Team Leader', 'C', 'N2')
        for i in range(4):
            self._AddPosition('Scout', 'C', 'E4')
