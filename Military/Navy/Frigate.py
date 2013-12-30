from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Navy.BaseClasses import Division, Department


class MasterAtArmsOffice(Unit):

    def _SetPositions(self):
        self._AddPosition('Master at Arms', 'W2', 'A', self)


class LegalDiv(Division):

    def _SetSubUnits(self):
        self._SubUnits.append(MasterAtArmsOffice(self))


class ExecutiveDiv(Division):
    pass


class SecurityDetachment(Unit):
    pass


class AstrogationDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Astrogation Officer', 'A', 'O2', self)


class BoatDiv(Division):
    pass


class CommunicationDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Communications Officer', 'A', 'O2', self)


class DeckDiv(Division):
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


class SupplyAdminDiv(Division):
    pass


class FoodServiceDiv(Division):
    pass


class SalesServicesDiv(Division):
    pass


class CargoDiv(Division):
    pass


class SickBay(Division):

    def _SetPositions(self):
        self._AddPosition('Assistant Medical Officer', 'A', 'O1', self)
        for i in range(2):
            self._AddPosition('Sick Bay Attendant', 'A', 'E4', self)


class SupplyDept(Department):

    def _SetSubUnits(self):
        self._SubUnits.append(SupplyAdminDiv(self))
        self._SubUnits.append(FoodServiceDiv(self))
        self._SubUnits.append(SalesServicesDiv(self))
        self._SubUnits.append(CargoDiv(self))

    def _SetPositions(self):
        self._AddPosition('Supply Officer', 'A', 'O2', self)


class AdminDept(Department):

    def _SetSubUnits(self):
        self._SubUnits.append(ExecutiveDiv(self))
        self._SubUnits.append(LegalDiv(self))


class TacticalDept(Department):

    def _SetSubUnits(self):
        self._SubUnits.append(MissileDiv(self))
        self._SubUnits.append(OrdnanceDiv(self))
        self._SubUnits.append(SensorDiv(self))
        self._SubUnits.append(WeaponsDiv(self))

    def _SetPositions(self):
        self._AddPosition('Tactical Officer', 'A', 'O3', self)
        self._AddPosition('Assistant Tactical Officer', 'A', 'O2', self)
        for i in range(2):
            self._AddPosition('Junior Tactical Officer', 'A', 'O1', self)


class EngineeringDept(Department):

    def _SetSubUnits(self):
        self._SubUnits.append(AuxiliaryDiv(self))
        self._SubUnits.append(DamageControlDiv(self))
        self._SubUnits.append(DeckDiv(self))
        self._SubUnits.append(ImpellerDiv(self))
        self._SubUnits.append(ReactorDiv(self))
        self._SubUnits.append(SailsDiv(self))

    def _SetPositions(self):
        self._AddPosition('Engineering Officer', 'A', 'O3', self)


class OperationsDept(Department):

    def _SetSubUnits(self):
        self._SubUnits.append(AstrogationDiv(self))
        self._SubUnits.append(BoatDiv(self))
        self._SubUnits.append(CommunicationDiv(self))
        self._SubUnits.append(DeckDiv(self))

    def _SetPositions(self):
        self._AddPosition('Operations Officer', 'A', 'O3', self)


class MedicalDept(Department):

    def _SetSubUnits(self):
        self._SubUnits.append(SickBay(self))

    def _SetPositions(self):
        self._AddPosition('Medical Officer', 'A', 'O3', self)


class Frigate(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(AdminDept(self))
        self._SubUnits.append(TacticalDept(self))
        self._SubUnits.append(EngineeringDept(self))
        self._SubUnits.append(MedicalDept(self))
        self._SubUnits.append(OperationsDept(self))

    def _SetPositions(self):
        self._AddPosition('Commanding Officer', 'A', 'O4', self)
        self._AddPosition('Executive Officer', 'A', 'O3', self)
        self._AddPosition('Boatswain', 'A', 'N5', self)
