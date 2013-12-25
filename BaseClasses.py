class Equipment(object):
    pass


class Location(object):
    pass


class Personnel(object):
    pass


class DObject(object):
    pass
'''
    _name = ''

    # Name Checking
    def _SetName(self, name):

        if not isinstance(name, str):
            print 'ERROR in RankCategory():'
            print 'Name must be a string!'
            exit(1)

        if not name[0].isupper():
            print 'ERROR in RankCategory():'
            print 'Name must be capitalized!'
            exit(1)

        self._name = name

    def __repr__(self):
        return self._name + ' at ' + hex(id(self))
'''