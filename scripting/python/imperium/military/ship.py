# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/military.ship.py
# Description     :Set of basic classes for inheritance
# Author          :Todd Doughty
# Date            :5 Jul 2014
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

from imperium.military.navy.base_classes import Division, Department


class Facility(object):

    def __init__(self, name, div=None, dept=None):

        self._name = name
        self._SetPositions()
        self._SetDivision(div)
        self._SetDepartment(dept)

    def _SetPositions(self):
        pass

    def _SetDivision(self, div):

        if not isinstance(div, Division):
            print 'ERROR in Facility._SetDivision:'
            print 'Division must be a division object!'
            exit(1)

        self._Division = div

    def _SetDepartment(self, dept):

        if dept is None:
            dept = self._Division._CmdUnit

        if not isinstance(dept, Department):
            print 'ERROR in Facility._SetDepartment:'
            print 'Department must be a department object!'
            exit(1)

        self._Department = dept


class Deck(object):

    def __init__(self):
        self._Facility = []
        self._SetFacilities()

    def _SetFacilities(self, name=None):
        pass
