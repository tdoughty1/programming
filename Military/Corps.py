from Imperium.Military.BaseClasses import Unit, Position


class Division(Unit):

    def __init__(self):
        Unit.__init__(self)


class Brigade(Unit):

    def __init__(self):
        Unit.__init__(self)


class Battalion(Unit):

    def __init__(self):
        Unit.__init__(self)


class Regiment(Unit):

    def __init__(self):
        Unit.__init__(self)


class Company(Unit):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(Platoon(self))

    def _SetTOE(self):

        self._TOE.append(Position('Commanding Officer', 'C', rank='O3', unit=self))
        self._TOE.append(Position('Executive Officer', 'C', rank='O2', unit=self))
        self._TOE.append(Position('First Sergeant', 'C', rank='N4', unit=self))
        self._TOE.append(Position('Clerk', 'C', rank='N1', unit=self))
        Unit._SetTOE(self)


class Platoon(Unit):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(Squad(self))

    def _SetTOE(self):
        self._TOE.append(Position('Platoon Leader', 'C', rank='O1', unit=self))
        self._TOE.append(Position('Platoon Sergeant', 'C', rank='N3', unit=self))
        Unit._SetTOE(self)


class Section(Unit):

    def __init__(self):
        Unit.__init__(self)


class Squad(Unit):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(Team(self))

    def _SetTOE(self):
        self._TOE.append(Position('Squad Sergeant', 'C', rank='N2', unit=self))
        Unit._SetTOE(self)


class Team(Unit):

    def _SetTOE(self):
        Roles = ['Team', 'Ready', 'Assist', 'Fire', 'Scout']
        count = 0
        for role in Roles:
            if count == 0:
                self._TOE.append(Position(role, 'C', rank='N1', unit=self))
            else:
                self._TOE.append(Position(role, 'C', rank='E4', unit=self))

            count += 1
