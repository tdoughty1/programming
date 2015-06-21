# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/base_classes.py
# Description     :Set of basic classes for inheritance
# Author          :Todd Doughty
# Date            :5 Jul 2014
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

""" imperium/base_classes.py

Module containing the base class from which most other classes are
derived from.

    Classes:
        ImpObject - Base class for most Imperium classes.
"""


class ImpObject(object):
    """ Base class from which many Imperium classes are derived.

        The primary purpose is to attach to each Imperium class a counter to
        keep track of the number of objects of that class and a list to store
        pointers to all the members of the class.

        Additionally, has attributes inherited by all objects.

        Attributes:
            _name: (string) - Name of the given object.

        Class Attributes:
            _counter: (int) - Current count of the objects created of the given
                class derived from ImpObject.
            _datalist: (list) - pointers to all created objects of the given
                class derived from ImpObject.

        Hidden Methods:
            _SetName: Stores given name to object.

    """

    def __init__(self):
        """ Constructs object of a class derived for ImpObject.

            This consists of two parts:
                1) First add a pointer to the class of the object that
                    is created and increment the counter by 1.
                2) Create an empty name attribute.
        """

        try:
            type(self)._datalist.append(self)
            type(self)._number += 1
        except AttributeError:
            type(self)._datalist = [self]
            type(self)._number = 1

        self._name = None

    def __repr__(self):
        if self._name:
            return self._name + ' at ' + hex(id(self))
        else:
            class_name = str(self.__class__).split('.')[-1]
            return class_name + ' at ' + hex(id(self))
    
    def __str__(self):
        return repr(self)

    # Name Checking
    def _SetName(self, name):
        """ Sets the name of the current object.

        Hidden method of any object derived from the ImpObject class.

        Parameters:
            name: (string) - The name of the created object.  Should be
                capitalized.

        Raises:
            TypeError: If name isn't a string.
            ValueError: If name isn't capitalized.
        """

        if not isinstance(name, str):
            raise TypeError('Name must be a string!')

        if not name[0].isupper():
            raise ValueError('Name must be capitalized!')

        self._name = name

