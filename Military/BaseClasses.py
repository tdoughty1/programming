class Unit(object):

    def __init__(self, cmdUnit=None):

        # Initialize Class Counter
        try:
            type(self)._datalist
        except(AttributeError):
            type(self)._datalist = []
            type(self)._number = 0

        self._CmdUnit = cmdUnit
        self._SubUnits = []

        self._Roster = []

        self._SetSubUnits()
        self._SetRoster()
        self._Add2Class()

    def _SetSubUnits(self):
        pass

    def _SetRoster(self):

        for unit in self._SubUnits:
            self._Roster.extend(unit._Roster)

    def _Add2Class(self):
        type(self)._datalist.append(self)
        type(self)._number += 1

    def __len__(self):
        return len(self._Roster)


class Position(object):

    def __init__(self, name, unit=None):

        self._position = name
        self._unit = unit

    def __repr__(self):
        return self._position + ' at ' + hex(id(self))
