from Imperium.BaseClasses import DObject
from Imperium.Military.BaseClasses import Unit


class Division(Unit):
    pass


class Department(Unit):
    pass


class Ship(Unit):
    pass


class ShipClass(DObject):
    pass


class ShipType(DObject):

    def _init__(self, name, code=None):
        DObject.__init__(self, name)
        self._SetCode(code)

    def _SetCode(self, code):
        self._code = code