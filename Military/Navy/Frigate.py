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
    pass


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
    pass


class AdminDept(Department):
    pass


class TacticalDept(Department):
    pass


class EngineeringDept(Department):
    pass


class OperationsDept(Department):
    pass


class MedicalDept(Department):
     class


class FrigateOrg(Unit):
    
    def _SetRoster(self):
        self._AddPosition('Commanding Officer', 'O3', 'N', self)
