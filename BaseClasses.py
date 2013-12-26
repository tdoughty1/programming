class DObject(object):

    def __init__(self):

        try:
            type(self)._datalist.append(self)
            type(self)._number += 1
        except(AttributeError):
            type(self)._datalist = [self]
            type(self)._number = 1

        self._datalist = None
        self._number = None

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
