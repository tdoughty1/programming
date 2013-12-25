from Imperium.Military.BaseClasses import Unit


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

    _datalist = []
    _number = 0

    def __init__(self):
        Unit.__init__(self)

        self._Roster['Commanding Officer'] = {}
        self._Roster['Executive Officer'] = {}
        self._Roster['First Sergeant'] = {}
        self._Roster['Clerk'] = {}

        # Create SubUnits
        for i in range(3):
            self._SubUnits.append(Platoon(self))

        # Add to Roster
        i = 0
        for unit in self._SubUnits:
            i += 1
            for key in unit._Roster:
                self._Roster[key + ' ' + str(i)] = unit._Roster[key]

        Company._datalist.append(self)
        Company._number += 1


class Platoon(Unit):

    _datalist = []
    _number = 0

    def __init__(self, cmd):
        Unit.__init__(self)

        self._Roster['Platoon Leader'] = {}
        self._Roster['Platoon Sergeant'] = {}

        # Link to Command Unit
        self._CmdUnit = cmd

        # Create SubUnits
        for i in range(3):
            self._SubUnits.append(Squad(self))

        # Add to Roster
        i = 0
        for unit in self._SubUnits:
            i += 1
            for key in unit._Roster:
                self._Roster[key + ' ' + str(i)] = unit._Roster[key]

        Platoon._datalist.append(self)
        Platoon._number += 1


class Section(Unit):

    def __init__(self):
        Unit.__init__(self)


class Squad(Unit):

    _datalist = []
    _number = 0

    def __init__(self, cmd):
        Unit.__init__(self)

        self._Roster['Squad Sergeant'] = {}

        # Link Command Unit
        self._CmdUnit = cmd

        # Create SubUnits
        for i in range(3):
            self._SubUnits.append(Team(self))

        # Add to Roster
        i = 0
        for unit in self._SubUnits:
            i += 1
            for key in unit._Roster:
                self._Roster[key + ' ' + str(i)] = unit._Roster[key]

        Squad._datalist.append(self)
        Squad._number += 1


class Team(Unit):

    _datalist = []
    _number = 0

    def __init__(self, cmd):

        Unit.__init__(self)

        # Link Command Unit
        self._CmdUnit = cmd

        Roles = ['Team', 'Ready', 'Assist', 'Fire', 'Scout']

        for role in Roles:
            self._Roster[role] = {}

        Team._datalist.append(self)
        Team._number += 1

        self._name = cmd._name + ': Team ' + str(len(cmd._SubUnits) + 1)
