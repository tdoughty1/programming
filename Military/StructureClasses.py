from sys import exit

from Imperium.BaseClasses import DObject

##############################################################################
# Basic Military Structure Classes
##############################################################################


class Rank(DObject):

    _datalist = []
    _number = 0

    def __init__(self, name, level, branch, category):

        self._SetName(name)
        self._SetBranch(branch)
        self._SetCategory(category)
        self._SetLevel(level)

        Rank._datalist.append(self)
        Rank._number += 1

    def __str__(self):
        return self._category._name[0] + str(self._level) + ' ' + \
            str(self._name)

    ##########################################################################
    # Initialization Helper functions
    ##########################################################################
    # Level Checking
    def _SetLevel(self, level):

        if not isinstance(level, int):
            print 'ERROR in Rank():'
            print 'Rank Level must be an integer value!'
            exit(1)

        blim = self._category._range[0]
        tlim = self._category._range[1]

        if level > tlim or level < blim:
            print 'ERROR in Rank():'
            print 'Rank Level must be in the range for the Rank Category!'
            exit(1)

        self._level = level

    # Category Checking
    def _SetCategory(self, category):

        from Imperium.Military.StructureClasses import RankCategory

        if not isinstance(category, RankCategory):
            print 'ERROR in Rank():'
            print 'Rank Category must be a rank category object!'
            exit(1)

        if self._branch[0] not in category._branch:
            print 'ERROR in Rank():'
            print 'Rank Category must be included in branch!'
            exit(1)

        self._category = category

    # Branch Checking
    def _SetBranch(self, branch):

        from Imperium.Military.StructureClasses import Branch

        self._branch = []

        if isinstance(branch, list) or isinstance(branch, tuple):

            for b in branch:

                if not isinstance(b, Branch):
                    print 'ERROR in Rank():'
                    print 'Branch must be a branch object!'
                    exit(1)

                self._branch.append(b)

            return

        if not isinstance(branch, Branch):
            print type(b)
            print 'ERROR in Rank():'
            print 'Branch must be a branch object!'
            exit(1)

        self._branch.append(branch)

    ##########################################################################
    # Comparative Functions
    ##########################################################################
    def __gt__(self, other):
        Order = ['Enlisted', 'Non-Commissioned Officer', 'Warrant Officer',
                 'Officer']
        # For same category ranks
        if self._category == other._category:
            return self._level > other._level

        # If self is Warrant Officer and other is Officer - 3 Offset
        elif(self._category._name == Order[2] and
             other._category._name == Order[3]):
            return self._level > other._level + 3

        # If self is Warrant Officer and other is NCO - 4 Offset
        elif(self._category._name == Order[2] and
             other._category._name == Order[1]):
            return self._level > other._level - 4

        # If self is Warrant Officer and other is Officer - 3 Offset
        elif(other._category._name == Order[2] and
             self._category._name == Order[3]):
            return other._level > self._level + 3

        # If other is Warrant Officer and self is NCO - 4 Offset
        elif(other._category._name == Order[2] and
             self._category._name == Order[1]):
            return other._level > self._level - 4

        # Otherwise can determine from category
        else:
            return self._category > other._category

    def __ge__(self, other):
        Order = ['Enlisted', 'Non-Commissioned Officer', 'Warrant Officer',
                 'Officer']
        # For same category ranks
        if self._category == other._category:
            return self._level >= other._level

        # If self is Warrant Officer and other is Officer - 3 Offset
        elif(self._category._name == Order[2] and
             other._category._name == Order[3]):
            return self._level >= other._level + 3

        # If self is Warrant Officer and other is NCO - 4 Offset
        elif(self._category._name == Order[2] and
             other._category._name == Order[1]):
            return self._level >= other._level - 4

        # If self is Warrant Officer and other is Officer - 3 Offset
        elif(other._category._name == Order[2] and
             self._category._name == Order[3]):
            return other._level >= self._level + 3

        # If other is Warrant Officer and self is NCO - 4 Offset
        elif(other._category._name == Order[2] and
             self._category._name == Order[1]):
            return other._level >= self._level - 4

        # Otherwise can determine from category
        else:
            return self._category > other._category

    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other

    ##########################################################################
    # Public Functions
    ##########################################################################
    def GetCode(self):
        return self._category._name[0] + str(self._level)

    def GetBranches(self):
        return self._branch


class Branch(DObject):

    _datalist = []
    _number = 0

    def __init__(self, name=None):
        self._SetName(name)

        Branch._datalist.append(self)
        Branch._number += 1

    def __repr__(self):
        return self._name + ' at ' + hex(id(self))

    def GetCode(self):
        return self._name[0]


class RankCategory(DObject):

    _datalist = []
    _number = 0

    def __init__(self, name=None, branch=None, range_=None):

        self._SetName(name)
        self._SetBranch(branch)
        self._SetRange(range_)

        RankCategory._datalist.append(self)
        RankCategory._number += 1

    ###########################################################################
    # Initialization Helper functions
    ###########################################################################

    # Branch Checking
    def _SetBranch(self, branch):

        self._branch = []

        if isinstance(branch, list) or isinstance(branch, tuple):

            for b in branch:

                if not isinstance(b, Branch):
                    print 'ERROR in RankCategory():'
                    print 'Branch must be a branch object!'
                    exit(1)

                self._branch.append(b)

            return

        if not isinstance(branch, Branch):
            print type(b)
            print 'ERROR in RankCategory():'
            print 'Branch must be a branch object!'
            exit(1)

        self._branch.append(branch)

    # Rank Range Checking
    def _SetRange(self, range_):

        if type(range_) == int:
            self._range = (0, range_)
            return

        if type(range_) == list or type(range_) == tuple:

            if len(range_) == 1 and isinstance(range[0], int):
                self._range(0, range_)
                return

            elif len(range_) == 2:

                if(isinstance(range_[0], int) and
                   isinstance(range_[1], int)):

                    if range_[0] > range_[1]:
                        self._range = (range_[1], range_[0])
                        return
                    else:
                        self._range = (range_[0], range_[1])
                        return

        print 'ERROR in RankCategory():'
        print 'Range must be defined with 1 or 2 integers!'
        exit(1)

    ###########################################################################
    # Comparative Functions
    ###########################################################################
    def __gt__(self, other):
        Order = ['Enlisted', 'Non-Commissioned Officer', 'Warrant Officer',
                 'Officer']
        return Order.index(self._name) > Order.index(other._name)

    def __ge__(self, other):
        Order = ['Enlisted', 'Non-Commissioned Officer', 'Warrant Officer',
                 'Officer']
        return Order.index(self._name) >= Order.index(other._name)

    def __lt__(self, other):
        Order = ['Enlisted', 'Non-Commissioned Officer', 'Warrant Officer',
                 'Officer']
        return Order.index(self._name) < Order.index(other._name)

    def __le__(self, other):
        Order = ['Enlisted', 'Non-Commissioned Officer', 'Warrant Officer',
                 'Officer']
        return Order.index(self._name) <= Order.index(other._name)

##############################################################################
# Helper Military Structure Classes
##############################################################################


class Branched(object):

    def _SetBranch(self, branch):

        if branch is None:
            self._branch = None

        if isinstance(branch, Branch):
            self._branch = branch
            return

        if isinstance(branch, str):
            for branchCheck in Branch._datalist:
                if branch == branchCheck.GetCode():
                    self._branch = branchCheck
                    return

        # Shouldn't make it here
        print 'ERROR in _SetBranch():'
        print 'Branch must be a valid branch object or branch code!'
        exit(1)


class Ranked(object):

    def _SetRank(self, rank):

        if rank is None:
            self._rank = None

        if isinstance(rank, Rank):
            self._rank = rank
            return

        if isinstance(rank, str):
            for rankCheck in Rank._datalist:
                if rank == rankCheck.GetCode():
                    if self._branch in rankCheck.GetBranches():
                        self._rank = rank
                        return

        print 'ERROR in Position():'
        print 'Rank must be a valid rank object or rank code!'
        exit(1)
