# -*- coding: utf-8 -*-
#!/usr/bin/env python
#======================================================================
# Title           :imperium.military.core.branch
# Description     :Set of military branch related classes.
# Author          :Todd Doughty
# Date            :29 Jun 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
#======================================================================

""" imperium/military/core/branch.py

Module containing basic military branch strucutres

    Virtual Classes
        Branched - Derives objects containing a branch class

    Classes:
        Branch - Examples: Navy, Army, etc.
"""

# File metadata
__license__ = "The MIT License (MIT)"
__copyright__ = "Copyright (c) 2015 Todd Doughty"
__version__ = "0.1"
__docformat__ = 'reStructuredText'

# Import Project Specific Modules
from imperium.base_classes import ImpObject
from imperium.core.sql_ext import TableCreate, TableFill, TableDrop, TableExist

#######################################################################
# Military Structure Virtual Classes
#######################################################################

class Branched(object):
    """ A virtual class used to derive an object which is in a branch.

        Attributes:
            _branches: (Branch) - The branch of a given object.

        Methods:
            SetBranches: Link a branch or collection of branches to
            derived object.
        
        Hidden Methods:
            _CheckBranch: 
    """

    def SetBranches(self, branch):
        """ Sets the branch property of the current object.

            Adds a single branch or list of branches to an object that
            inherits the Branched virtual class.

            Parameters:
                branch (Branch) (str) (list) (tuple) - A branch object
                    from the current environment. Can submit a single
                    branch object, the branch name, or branch code; or
                    a list or tuple of them. Examples are Navy, Marine,
                    etc.

            Raises:
                TypeError: If branch is not a Branch object, name, or
                    code (string).
                ValueError: If branch code (string) is not linked to a
                    valid branch object.
        """

        if branch is None:
            self._branch = None
            return

        if self._CheckBranch(branch):
            self._branch = branch
            return

        if isinstance(branch, list) or isinstance(branch, tuple):

            tempBranches = []
            for branch in branches:
                if _CheckBranch(branch):
                    tempBranches.append(branch)

            if len(tempBranches) == branches:
                self._branches = branches
                return

        raise TypeError('Branches must be valid branch objects, ' +
                        'codes, or names!')

    def _CheckBranch(self, branch):
        """ Checks the input branch is a valid object.

            Helper function to validate the input branch for the 
            _SetBranch function.

            Parameters:
                branch (Branch) (str) (list) (tuple) - A branch object
                    from the current environment. Can submit a single
                    branch object, the branch name, or branch code; or
                    a list or tuple of them. Examples are Navy, Marine,
                    etc.

            Raises:
                TypeError: If branch is not a Branch object, name, or
                    code (string).
                ValueError: If branch code (string) is not linked to a
                    valid branch object.
        """        
        if isinstance(branch, Branch):
            return branch
        
        if isinstance(branch, str)
            for branchCheck in Branch._datalist:
                if(branch == branchCheck.GetCode() or 
                   branch == branchCheck.GetName():
                    return branchCheck
            
            raise ValueError('Branch must be a valid branch code!')
            
        raise TypeError('Branches must be valid branch objects, ' +
                        'codes, or names!')


#######################################################################
# Basic Military Structure Classes
#######################################################################

class Branch(ImpObject):
    """ A class used to represent a branch of the military.

        Examples are Army, Navy, etc.

        Attributes:
            _name: (string) - Name of the Branch

        Hidden Methods:
            _SetName: Set the name of the branch.

        Methods:
            GetCode: Returns code corresponding to the given branch.
                This is currently always the first letter of the name.
                #TODO - Add option to override default behavior.
    """

    def __init__(self, name, code=None):
        """ Constructs the military branch.

            Parameters:
                name: (string) - Name of the given military branch.
        """

        ImpObject.__init__(self)

        self._SetName(name)

    def GetCode(self):
        """ Return the code (string) corresponding the given branch.

            Currently this is forced to be the first letter of the
            branch name.
            #TODO - Allow an additional code option to be set.
        """
        return self._name[0]




def _Fill():

    

Branches.append(Branch('Admiralty'))
Branches.append(Branch('Legion'))
Branches.append(Branch('Corps'))
