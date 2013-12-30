class LegalDiv(Division):
    pass
    

class ExecutiveDiv(Division):
    pass


class SecurityDetachment(Unit):
    pass


class AstrogationDiv(Division):
    pass


class BoatDiv(Division):
    pass


class CommunicationDiv(Division):
    
    def _SetRoster(self):
        self._AddPosition('Communications Officer', 'O2', 'A', self)


class AuxiliaryDiv(Division):
    pass


class DamageControlDiv(Division):
    pass


class ImpellerDiv(Division):
    pass
   

class ReactorDiv(Division):
     pass


class SailsDiv(Division):
    pass


class MissileDiv(Division):
    pass


class OrdnanceDiv(Division):
    pass


class WeaponsDiv(Division):
    pass


class SensorDiv(Division):
    pass


class SupplyDept(Department):
    
    def _SetRoster(self):
        self._AddPosition('Supply Officer', 'O2', 'A', self)


class AdminDept(Department):
    pass


class TacticalDept(Department):
    
    def _SetRoster(self):
        self._AddPosition('Tactical Officer' ,'O3','A', self)
        self._AddPosition('Assistant Tactical Officer', 'O2', 'A', self)
        for i in range(2):
            self._AddPosition('Junior Tactical Officer', 'O1', 'A', self)


class EngineeringDept(Department):
    
    def _SetRoster(self):
        self._AddPosition('Engineering Officer', 'O3', 'A', self)


class OperationsDept(Department):
    
    def _SetRoster(self):
        self._AddPosition('Operations Officer', 'O3', 'A', self)


class MedicalDept(Department):
     class


class FrigateOrg(Unit):
    
    def _SetRoster(self):
        self._AddPosition('Commanding Officer', 'O4', 'A', self)
        self._AddPosition('Executive Officer', 'O3', 'A', self)
        self._AddPosition('Boatswain', 'N5', 'A', self)
