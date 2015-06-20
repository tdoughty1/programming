from Imperium.BaseClasses import ImpObject
from Imperium.Military.BaseClasses import Unit


class Division(Unit):
    pass


class Department(Unit):
    pass


class Ship(Unit):
    pass


class ShipClass(ImpObject):
    pass


class ShipType(ImpObject):

    def _SetCode(self, code):
        self._code = code
