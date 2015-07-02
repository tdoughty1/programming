from angles import Angle as angle
from random import random
from numpy import log2, modf, tan, pi


class Star(object):

    def __init__(self, system, loc=None, name=None, stype=None):

        self._x = loc[0]
        self._y = loc[1]
        self._z = loc[2]

        self._name = name
        self._stype = stype

    def RandomStarType(num=1):
        types = 'OBAFGKM'

        stypes = []
        for i in range(num):
            data = modf(log2(2**len(types)*random()))
            stypes.append(types[int(data[1])] + str(int(10*data[0])))

        return stypes


class System(object):

    def __init__(self, loc, name=None):

        x = loc[0]
        y = loc[1]
        z = loc[2]

        r = np.sqrt(x**2 + y**2 + z**2)
        phi = angle(atan(y / x) * 180 / pi)
        theta = angle(atan(z / (x**2 + y**2)) * 180 / pi)

        self._x = x
        self._y = y
        self._z = z

        self._r = r
        self._phi = phi
        self._theta = theta

        self._name = name
        self._stars = []

    def RightAscension(self):
        # TODO - Fix actual definition
        print '%02dh, %02dm, %4.2f' % (self._phi, self._phi, self._phi)

    def Declination(self):
        pass

    def Distance(self, other=None):
        if other is None:
            return self._r
        else:
            return np.sqrt((self._x - other._x)**2 +
                           (self._y - other._x)**2 +
                           (self._z - other._z)**2)
