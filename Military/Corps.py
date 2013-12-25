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

    def _SetRoster(self):

        self._Roster.append(Position('Commanding Officer', branch='C', rank='O3', unit=self))
        self._Roster.append(Position('Executive Officer', branch='C', rank='O2', unit=self))
        self._Roster.append(Position('First Sergeant', branch='C', rank='N4', unit=self))
        self._Roster.append(Position('Clerk', branch='C', rank='N1', unit=self))


class Platoon(Unit):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(Squad(self))

    def _SetRoster(self):
        self._Roster.append(Position('Platoon Leader', branch='C', rank='O1', unit=self))
        self._Roster.append(Position('Platoon Sergeant', branch='C', rank='N3', unit=self))
        Unit._SetRoster(self)


class Section(Unit):

    def __init__(self):
        Unit.__init__(self)


class Squad(Unit):

    def _SetSubUnits(self):
        for i in range(3):
            self._SubUnits.append(Team(self))

    def _SetRoster(self):
        self._Roster.append(Position('Squad Sergeant', branch='C', rank='N2', unit=self))
        Unit._SetRoster(self)


class Team(Unit):

    def _SetRoster(self):
        Roles = ['Team', 'Ready', 'Assist', 'Fire', 'Scout']
        count = 0
        for role in Roles:
            if count == 0:
                self._Roster.append(Position(role, branch='C', rank='N1', unit=self))
            else:
                self._Roster.append(Position(role, branch='C', rank='E4', unit=self))

            count += 1
