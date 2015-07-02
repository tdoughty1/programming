# -*- coding: utf-8 -*-
# !/usr/bin/env python
# =====================================================================
# Title           :imperium/military/corps/frigate.py
# Description     :Classes for Marine detachments on frigates
# Author          :Todd Doughty
# Date            :20 Jul 2015
# Version         :0.1
# Notes           :
# Python Version  :2.7.6
# =====================================================================

from imperium.military.base_classes import Unit
from detach_classes import PlatoonDet
#, CompanyDet_HQ_CO, CompanyHQ_XO, CompanyDet_HQ, CompanyDet
#from detach_classes import BattalionDet_HQ_CO, BattalionDet_HQ_XO, BattalionDet_HQ_S14, BattalionDet_HQ_S23, BattalionDet_HQ, BattalionDet
from imperium.military.corps.corps import RifleSquad


class LightPlatoonDet_FG(PlatoonDet):
    """Platoon detached for service on a frigate.

    Lighter than the standard platoon, it contains only two :class: 
    `RifleSquad`s instead of the standard three.
    """

    def _SetSubUnits(self):
        for i in range(2):
            self._SubUnits.append(RifleSquad(self))


class CompanyDet_HQ_CO_FG(CompanyDet_HQ_CO):
    """CO command element of a dispersed company for frigate service.

    The command element for a company that has been dispersed
    throughout all frigates of an element is split into two portions
    and each is attached to one of the :class:`LightPlatoonDet_FG`s.
    This element consists of the Commanding Officer (CO), the First
    Sergeant, the Quartermaster, and the clerk.
    """

    def _SetPositions(self):
        self._AddPosition('Commanding Officer', 'C', 'O3', self, pos=Pos)
        self._AddPosition('First Sergeant', 'C', 'N4', self, pos=Pos)
        self._AddPosition('Quartermaster', 'C', 'N2', self, pos=Pos)
        self._AddPosition('Clerk', 'C', 'N1', self, pos=Pos)


class CompanyDet_HQ_XO_FG(CompanyDet_HQ_XO):
    """XO command element of a dispersed company for frigate service.

    The command element for a company that has been dispersed
    throughout all frigates of an element is split into two portions
    and each is attached to one of the :class:`LightPlatoonDet_FG`s.
    This element consists of the Company Executive Officer (XO) and
    the Company Armourer.
    """

    def _SetPositions(self):
        Pos = self._CmdUnit._SubUnits[0]._TOE[0]
        self._AddPosition('Executive Officer', 'C', 'O2', self, pos=Pos)
        self._AddPosition('Armorer', 'C', 'N2', pos=Pos)
        self._AddPosition


class CompanyDet_HQ_FG(Company_Det_HQ):
    """A platoon detached for service on a frigate.

    Lighter than the standard platoon, it contains only two :class: 
    `Rifle_Squad`s instead of the standard three.
    
    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attribute and property types -- if given -- should be specified according
    to `PEP 484`_, though `PEP 484`_ conformance isn't required or enforced.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (Optional[int]): Description of `attr2`.


    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484/

    """
    
    def _SetSubUnits(self):
        CoHQ = self._CmdUnit._CmdUnit._SubUnits[0]._SubUnits[6]._SubUnits[1]
        CoHQ._AdmCmdUnit = self
        self._SubUnits.append(CoHQ)
        XoHQ = self._CmdUnit._CmdUnit._SubUnits[1]._SubUnits[6]._SubUnits[1]
        XoHQ._AdmCmdUnit = self
        self._SubUnits.append(XoHQ)


class CompanyDet_FG(CompanyDet):
    """A platoon detached for service on a frigate.

    Lighter than the standard platoon, it contains only two :class: 
    `Rifle_Squad`s instead of the standard three.
    
    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attribute and property types -- if given -- should be specified according
    to `PEP 484`_, though `PEP 484`_ conformance isn't required or enforced.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (Optional[int]): Description of `attr2`.


    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484/

    """
    
    def _SetSubUnits(self):
        for i in range(6):
            Platoon = self._CmdUnit._SubUnits[i]._SubUnits[6]._SubUnits[0]
            self._SubUnits.append(Platoon)
            Platoon._AdmCmdUnit = self
        self._SubUnits.append(Company_Det_HQ_FG(self))


class BattalionDet_HQ_CO_FG(BattalionDet_HQ_CO):
    """Commanding Officer's HQ element for disbursed frigate battalion.

    
    """
    
    def _SetPositions(self):
        Flot = self._CmdUnit._CmdUnit._CmdUnit
        CO = Flot._SubUnits[0]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[0]
        self._AddPosition('Battalion Commanding Officer', 'C', 'O5', self,
                          pos=CO)
        SM = Flot._SubUnits[0]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[1]
        self._AddPosition('Sergeant Major', 'C', 'N5', self, pos=SM)
        CM = Flot._SubUnits[0]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[2]
        self._AddPosition('Battalion Chief Medic', 'C', 'N3', pos=CM)


class BattalionDet_HQ_XO_FG(BattalionDet_HQ_XO):
    """A platoon detached for service on a frigate.

    Lighter than the standard platoon, it contains only two :class: 
    `Rifle_Squad`s instead of the standard three.
    
    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attribute and property types -- if given -- should be specified according
    to `PEP 484`_, though `PEP 484`_ conformance isn't required or enforced.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (Optional[int]): Description of `attr2`.


    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484/

    """
    
    def _SetPositions(self):
        Flot = self._CmdUnit._CmdUnit._CmdUnit
        CO = Flot._SubUnits[1]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[0]
        self._AddPosition('Battalion Executive Officer', 'C', 'O4', self,
                          pos=CO)


class BattalionDet_HQ_S14_FG(BattalionDet_HQ_S14):
    """A platoon detached for service on a frigate.

    Lighter than the standard platoon, it contains only two :class: 
    `Rifle_Squad`s instead of the standard three.
    
    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attribute and property types -- if given -- should be specified according
    to `PEP 484`_, though `PEP 484`_ conformance isn't required or enforced.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (Optional[int]): Description of `attr2`.


    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484/

    """

    def _SetPositions(self):
        Flot = self._CmdUnit._CmdUnit._CmdUnit
        AS = Flot._SubUnits[3]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[0]
        self._AddPosition('Battalion Adjutant/Supply Officer', 'C', 'O3', self,
                          pos=AS)
        BQ = Flot._SubUnits[3]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[3]
        self._AddPosition('Battalion Quartermaster', 'C', 'N3', self, pos=BQ)
        BC = Flot._SubUnits[3]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[4]
        self._AddPosition('Battalion Clerk', 'C', 'N3', pos=BC)


class BattalionDet_HQ_S23_FG(BattalionDet_HQ_S23):
    """A platoon detached for service on a frigate.

    Lighter than the standard platoon, it contains only two :class: 
    `Rifle_Squad`s instead of the standard three.
    
    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attribute and property types -- if given -- should be specified according
    to `PEP 484`_, though `PEP 484`_ conformance isn't required or enforced.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (Optional[int]): Description of `attr2`.


    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484/

    """

    def _SetPositions(self):
        Flot = self._CmdUnit._CmdUnit._CmdUnit
        OI = Flot._SubUnits[2]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[0]
        self._AddPosition('Battalion Intelligence/Operations Officer', 'C',
                          'O4', self, pos=OI)
        OC = Flot._SubUnits[2]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[1]
        self._AddPosition('Battalion Operations Chief', 'C', 'N3', self,
                          pos=OC)
        IC = Flot._SubUnits[2]._AdminUnits[0]._SubUnits[6]._SubUnits[0]._TOE[2]
        self._AddPosition('Battalion Intelligence Chief', 'C', 'N2', self,
                          pos=IC)


class BattalionDet_HQ_FG(BattalionDet_HQ):
    """A platoon detached for service on a frigate.

    Lighter than the standard platoon, it contains only two :class: 
    `Rifle_Squad`s instead of the standard three.
    
    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attribute and property types -- if given -- should be specified according
    to `PEP 484`_, though `PEP 484`_ conformance isn't required or enforced.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (Optional[int]): Description of `attr2`.


    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484/

    """
    
    def _SetSubUnits(self):
        self._SubUnits.append(Battalion_Det_HQ_CO_FG(self))
        self._SubUnits.append(Battalion_Det_HQ_XO_FG(self))
        self._SubUnits.append(Battalion_Det_HQ_S23_FG(self))
        self._SubUnits.append(Battalion_Det_HQ_S14_FG(self))


class BattalionDet_FG(BattalionDet):
    """A platoon detached for service on a frigate.

    Lighter than the standard platoon, it contains only two :class: 
    `Rifle_Squad`s instead of the standard three.
    
    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attribute and property types -- if given -- should be specified according
    to `PEP 484`_, though `PEP 484`_ conformance isn't required or enforced.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (Optional[int]): Description of `attr2`.


    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484/

    """

    def _SetSubUnits(self):
        for i in range(4):
            Company = self._CmdUnit._SubUnits[i]._AdminUnits[0]
            self._SubUnits.append(Company)
            Company._AdmCmdUnit = self
        self._SubUnits.append(Battalion_Det_HQ_FG(self))
'''
