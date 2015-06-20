# -*- coding: utf-8 -*-
#!/usr/bin/env python
#===============================================================================
# Title           :StructureClasses.py
# Description     :Set of basic classes for inheritance
# Author          :Todd Doughty
# Date            :5 Jul 2014
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
#===============================================================================

""" StructureClasses.py

Module containing basic military structure classes and corresponding virtual
classes.

    Virtual Classes
        Branched - Derives objects containing a branch class
        Ranked - Derives objects containing a rank class

    Classes:
        Branch: Navy, Army, etc.
        Rank Category: Officer, Enlisted, etc.
        Rank: Captain, Colonel, etc.
"""

# Import Project Specific Modules
from Imperium.BaseClasses import ImpObject

###############################################################################
# Military Structure Virtual Classes
###############################################################################

class Branched(object):
    """ A virtual class used to derive an object which is part of a branch.

        Attributes:
            _branch: (Branch) - The branch of a given object.

        Hidden Methods:
            _SetBranch: Link a branch to derived object.
    """

    def _SetBranch(self, branch):
        """ Sets the branch property of the current object.

            A hidden function of the Branched class object.

            Parameters:
                branch: (Branch) - A branch object from the current environment.
                    Examples are Navy, Marine, etc.

            Raises:
                TypeError: If branch is not a Branch object or code (string).
                ValueError: If branch code (string) is not linked to a valid
                    branch object.
        """

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
            raise ValueError('Branch must be a valid branch code!')

        raise TypeError('Branch must be a valid branch object or branch code!')

class Ranked(object):
    """ A virtual class used to derive an object which has a rank.

        Attributes:
            _rank: (Rank) - A rank object.

        Hidden Methods:
            _SetRank - Add a rank to derived object.
    """

    def _SetRank(self, rank):
        """ Sets the base rank property of the current object.

            A hidden method of the Ranked class object.

            Parameters:
                rank: (Rank) or (string) - A rank object or a valid rank code
                    from the current environment.  Examples are Lieutenant J.G.,
                    Field Marshal, etc.

            Raises:
                TypeError: If rank is not an object or a rank code (string).
                ValueError: If rank is a code (string), but not linked to a
                    valid rank.
        """

        if rank is None:
            self._rank = None
            return

        if isinstance(rank, Rank):
            self._rank = rank
            self._posrank = {'ranks':[rank], 'probs':[1]}
            return

        if isinstance(rank, str):
            for rankCheck in Rank._datalist:
                if rank == rankCheck.GetCode():
                    if self._branch in rankCheck.GetBranches():
                        self._rank = rankCheck
                        self._posrank = {'ranks':[rankCheck], 'probs':[1]}
                        return
            raise ValueError('Rank must be a valid rank code!')

        raise TypeError('Rank must be a valid rank object or rank code!')


    def _AddPosRank(self, rank, probability):
        """ Adds possible ranks and their corresponding probabilities 
            to the current object.

            A hidden method of the Ranked class object.

            Parameters:
                rank: (Rank), (string), (list), or (tuple) - A rank
                   object, a valid rank code, or a list/tuple of either
                   option from the current environment.  Examples are
                   Lieutenant J.G., Field Marshal, etc.
                probability (float), (tuple) or (list) - The probability
                    that a randomly generated individual for the
                    corresponding position will have the corresponding
                    rank. If a list is input for the rank, it must be of
                    equal length to the rank array.  The probability
                    must be valid (0-1), but also ensure that the total
                    probability is less than 1 and the base rank is the
                    most probable.

            Raises:
                TypeError: If rank is not a rank object or a rank code
                    (string), or a (list/tuple) of them.
                ValueError: If rank is a code (string), but not linked
                    to a valid rank, or the list is the wrong length or
                    can't fulfill probablility requirements.
        """

        # First option - Rank Code - Convert to a Rank object
        if isinstance(rank, str):
            found = False
            for rankCheck in Rank._datalist:
                if rank == rankCheck.GetCode():
                    if self._branch in rankCheck.GetBranches():
                        rank = rankCheck
                        found = True
                        break
            if not found:
                raise ValueError('Rank must be a valid rank code!')

        # Second Option - Single Rank Object
        if isinstance(rank, Rank):
            if rank in self._posrank['ranks']:
                raise ValueError("Rank can't already be a possible rank!")
            
            # Ensure probability is a float
            if not isinstance(probability, float):
                raise TypeError('Rank Probability must be a float!')
            
            # Ensure there is a valid probability value (based on state
            # of self._posrank)
            
            # Probability must be greater than 0
            if probability < 0:
                raise ValueError('Rank Probability must be greater than 0!')
            
            if probability > 1:
                raise ValueError('Rank Probability must be less than 1')
            
            # The base probability must still be higher than the rest
            checkProb = max(max(self._posrank['probs'][1:]), probability) if len(self._posrank['probs'][1:]) > 0 else probability
            if self._posrank['probs'][0]-probability <= checkProb:
                    #TODO Add actual range to text
                    raise ValueError('Rank Probability must ensure that the total probabilty is less than 1, while the base rank is still most likely!')
            else:
                self._posrank['ranks'].append(rank)
                self._posrank['probs'][0] -= probability
                self._posrank['probs'].append(probability)
            
            return

        # Third option, 
        if isinstance(rank, list) or isinstance(rank, tuple):
            
            if len(rank) == len(probability):
                for r, p in zip(rank, probability):
                    self._AddPosRank(r, p)
            elif len(probability) != 1:
                for r in rank:
                    self._AddPosRank(r, probability)
            else:
                raise TypeError('Probability iterable must have the same length as rank, or be a single float!')
            
            return

        # Anything else should fail
        raise TypeError('Rank must be a valid rank object or rank code, or list/tuple of them!')

##############################################################################
# Basic Military Structure Classes
##############################################################################

class Branch(ImpObject):
    """ A class used to represent a branch of the military (other organization).

        Examples are Army, Navy, etc.

        Attributes:
            _name: (string) - Name of the Branch - Inherited from ImpObject

        Hidden Methods:
            _SetName: (Inherited from ImpObject) - Set the name of the branch.

        Methods:
            GetCode: Returns the code corresponding to the given branch.  This
                is currently always the first letter of the name.
                #FIXME - Add option to override default behavior.
    """

    def __init__(self, name):
        """ Constructs the military branch.

            Parameters:
                name: (string) - Name of the given military branch.
        """

        ImpObject.__init__(self)

        self._SetName(name)

    def GetCode(self):
        """ Return the code (string) corresponding the given branch.

            Currently this is forced to be the first letter of the branch name.
            #FIXME - Allow an additional code option to be set.
        """
        return self._name[0]


class RankCategory(ImpObject):
    """ A class used to represent a level of rank.

        Examples are Officer, Enlisted etc.

        Attributes:
            _name: (string) - Name of the category - Inherited from ImpObject
            _branch: (list) - List of Branches that have the category.

        Hidden Methods:
            _SetName: (Inherited from ImpObject) - Set the name of the category.
            _SetBounds: Set the upper and lower bounds of the category rank seniorities.
            _SetBranches: (Overwritten from ImpObject) - Set branches which have this category of rank.

        Methods:
            GetCode: Returns the code corresponding to the given branch.  This is currently always the first letter of the name. 
        
        #FIXME - Add option to override default behavior.

    """

    def __init__(self, name, bounds, branch):

        self._SetName(name)
        self._SetBounds(bounds)
        self._SetBranch(branch)

    ###########################################################################
    # Initialization Helper functions
    ###########################################################################

    # Branch Checking
    def _SetBranch(self, branch):
        """ Set list of branches that have this rank category.

            Parameters:
                branch: (list), (tuple), or (Branch) - Can input either a single
                    branch, or a list or tuple of branches.

            Raises:
                TypeError: If branch is neither a Branch object, nor a list or
                    tuple of branches.

        """
        self._branch = []

        if isinstance(branch, list) or isinstance(branch, tuple):

            for b in branch:

                if not isinstance(b, Branch):
                    raise TypeError('branch must be a Branch object!')

                self._branch.append(b)
            return

        if not isinstance(branch, Branch):
            raise TypeError('branch must be a Branch object!')
        self._branch.append(branch)

    # Rank Range Checking
    def _SetBounds(self, bounds):
        """ Set the upper and lower bounds for rank level for a given category.

            Parameters:
                bounds: (int), (list), or (tuple) - Either a single integer, or
                    a list or tuple of one or two integers.  Only one integer
                    assumes a lower bound of 0.

            Raises:
                ValueError: If a list or tuple of bounds, is neither 1 or 2.
                TypeError: If bounds is not an integer, list or tuple.
        """

        # If only a single value given, it's the upper bound
        if isinstance(bounds, int):
            self._range = (0, bounds)
            return

        # Can be given in a list or tuple
        if isinstance(bounds, (list, tuple)):

            # If only a single value given, it's the upper bound
            if len(bounds) == 1 and isinstance(bounds[0], int):
                self._range(0, bounds)
                return

            # If both bounds are given, check they are integers and store
            # upper and lower bounds.
            elif len(bounds) == 2:

                if(isinstance(bounds[0], int) and
                   isinstance(bounds[1], int)):

                    if bounds[0] > bounds[1]:
                        self._range = (bounds[1], bounds[0])
                        return
                    else:
                        self._range = (bounds[0], bounds[1])
                        return
                else:
                    raise TypeError('bounds must be integers!')
            else:
                raise ValueError('bounds must have length 1 or 2!')

        raise TypeError('bounds must be an integer, list of integers, or ' +
                        'tuple of integers!')

    ###########################################################################
    # Comparative Functions
    ###########################################################################

    #FIXME - Automate setup of comparisons

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


class Rank(ImpObject, Branched):
    """ A Miltary (or other organization) rank.

        Attributes:
            _name: (string) - Name of the given object.
            _branch: (Branch) - Branch which rank exists in (Army, Navy, etc.).
            _category: (RankCategory) - General category of the rank (Enlisted, Officer, etc.).
            _level: (int) - Relative seniority of rank in given category.
            _issplit: (bool) - Flag if rank is split into sublevels (Admiral of the Red, etc.).

        Optional Attributes:
            _sublevel: (int) - Relative seniority of split ranks.

        Methods:

        Hidden Methods:
            _SetName: (inherited from ImpObject) - Store name.
            _SetBranch: (inherited from Branched) - Link to branch object.
            _SetCategory: Link to category object.
            _SetLevel: Store level value.

    """

    def __init__(self, name, level, branch, category, split=False, slevel=None):
        """ Constructs a rank object.

            Creates a rank object, stores a pointer of that object in the
            datalist attribute of the rank class, and increments the rank class
            counter.

            Parameters:
                name: (string) - Name of rank.
                level: (int) - Relative seniority of rank, must be in the range
                    bounds set for the given category.
                branch:  (Branch) - Branch object that the rank is part of.
                category: (RankCategory) - RankCategory object that the rank is
                    part of.

            Optional (Keyword) Parameters:
                issplit: (bool) - Flag if the rank is a sublevel.  For instance
                    Rear Admiral of the Green.
                slevel: (+/-) - Relative seniority of the rank within the given
                    sublevel.
        """

        ImpObject.__init__(self)

        self._SetName(name)
        self._SetBranch(branch)
        self._SetCategory(category)
        self._SetLevel(level)

        self._issplit = split

        if self._issplit:
            if slevel not in ['+', '-']:
                raise ValueError("Split level must be either '+' or '-'")
                
            self._sublevel = slevel

    def __str__(self):
        
        if self._issplit and self._sublevel == '+':
            return self._category._name[0] + str(self._level) + \
                self._sublevel + ' ' + str(self._name)
        else:
            return self._category._name[0] + str(self._level) + ' ' + \
                str(self._name)

    ##########################################################################
    # Initialization Helper functions
    ##########################################################################
    # Level Checking
    def _SetLevel(self, level):
        """ Sets seniority level of the rank.

            Checks to see if the level of the rank is an integer within the
            limits set by the category bounds, then stores the value.

            Category must be set previously.

            Parameters:
                level: (int) - Seniority level of a given rank (ie O9 is "9").

            Raises:
                TypeError: If level is not an integer.
                ValueError: If level is not between category bounds.
        """
        if not isinstance(level, int):
            raise TypeError('Rank Level must be an integer value!')

        #FIXME - Use Attribute method instead of direct access
        blim = self._category._range[0]
        tlim = self._category._range[1]

        if tlim >= level >= blim:
            self._level = level
        else:
            raise ValueError('Rank Level must be in the range for the Rank' +
                             ' Category!')

    # Category Checking
    #FIXME - Logic may be off
    def _SetCategory(self, category):
        """ Link the rank category to the rank.

            Parameters:
                category: (RankCategory) - Link the rank to the category it is a
                    part of.

            Raises:
                TypeError: If category is not a RankCategory object.
                ValueError: If category doesn't include a branch that matches
                    rank branch. Branch must already be set.
        """

        if not isinstance(category, RankCategory):
            raise TypeError('Rank Category must be a rank category object!')

        #FIXME switch category branch access to method
        badBranch = False
        for branch in self._branch:
            if branch not in category._branch:
                badBranch = True

        if badBranch:
            raise ValueError('Rank Category must be included in branch!')

        self._category = category

    # Branch Checking
    def _SetBranch(self, branch):

        self._branch = []

        if isinstance(branch, (list, tuple)):

            for b in branch:

                if not isinstance(b, Branch):
                    raise TypeError('Branch must be a branch object!')

                self._branch.append(b)

            return

        if not isinstance(branch, Branch):
            raise TypeError('Branch must be a branch object!')
            exit(1)

        self._branch.append(branch)

    ##########################################################################
    # Comparative Functions
    ##########################################################################

    #FIXME - Switch to automated category order

    def __gt__(self, other):
        Order = ['Enlisted', 'Non-Commissioned Officer', 'Warrant Officer',
                 'Officer']
        # For same category ranks
        if self._category == other._category:
            if(self._issplit and other._issplit and
               self._level == other._level):
                if self._sublevel == '+' and other._sublevel == '-':
                    return True
                else:
                    return False
            else:
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
            if(self._issplit and other._issplit and
               self._level == other._level):
                if self._sublevel == other._sublevel or \
                  (self._sublevel == '+' and self._sublevel == '-'):
                    return True
                else:
                    return False
            else:
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
            return self._category >= other._category

    def __eq__(self, other):
        return self >= other and not self > other

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other

    ##########################################################################
    # Public Functions
    ##########################################################################
    def GetCode(self):
        """ Return the code (string) for this rank."""
        if self._issplit and self._sublevel == '+':
            return self._category._name[0] + str(self._level) + self._sublevel
        else:
            return self._category._name[0] + str(self._level)

    def GetBranches(self):
        """ Return list of branches which have this rank. """
        return self._branch
