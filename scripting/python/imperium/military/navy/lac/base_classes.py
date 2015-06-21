from Imperium.Military.BaseClasses import Unit


class LAC_Unit(Unit):

    def __init__(self, cmdUnit=None):

        if cmdUnit is not None:
            self._SetCallSign(cmdUnit)
        else:
            self._CallSign = ''
        Unit.__init__(self, cmdUnit)
