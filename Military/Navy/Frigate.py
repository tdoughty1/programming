from Imperium.Military.BaseClasses import Unit
from Imperium.Military.Navy.BaseClasses import Division, Department
from Imperium.Military.Corps.Frigate import LightPlatoon_Det_FG


class MasterAtArmsOffice(Unit):

    def _SetPositions(self):
        self._AddPosition('Master at Arms', 'A', 'W2', self)


class LegalDiv(Division):

    def _SetSubUnits(self):
        self._SubUnits.append(MasterAtArmsOffice(self))


class ExecutiveDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Yeoman', 'A', 'E4', self)


class SecurityDetachment(Unit):

    def _SetSubUnits(self):
        self._SubUnits.append(LightPlatoon_Det_FG(self))

    def _SetPositions(self):
        Pos = self._SubUnits[0]._TOE[0]
        self._AddPosition('Detachment Commander', 'A', 'O2', self, pos=Pos)


class AstrogationDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Astrogation Officer', 'A', 'O2', self)
        self._AddPosition('Quartermaster', 'A', 'N2', self)
        for i in range(2):
            self._AddPosition('Quartermaster Mate', 'A', 'E4', self)
        self._AddPosition('Helmsman', 'A', 'N1', self)
        for i in range(2):
            self._AddPosition('Helmsman', 'A', 'E4', self)


class BoatDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Boat Bay Officer', 'A', 'O1', self)
        self._AddPosition('Pilot', 'A', 'N2', self)
        self._AddPosition('CoPilot', 'A', 'N1', self)
        self._AddPosition('Crew Chief', 'A', 'N1', self)
        for i in range(3):
            self._AddPosition('Crewmen', 'A', 'E4', self)


class CommunicationDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Communications Officer', 'A', 'O2', self)
        for i in range(2):
            self._AddPosition('Crewmen', 'A', 'E4', self)


class DeckDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Deck Officer', 'A', 'O1', self)
        self._AddPosition('Deck Chief', 'A', 'N2', self)
        for i in range(3):
            self._AddPosition('Watch Chief', 'A', 'N1', self)
            for j in range(4):
                self._AddPosition('Deck Crew', 'A', 'E4', self)


class AuxiliaryDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Auxiliary Officer', 'A', 'O1', self)
        for i in range(3):
            self._AddPosition('Watch Chief', 'A', 'N1', self)
            for j in range(4):
                self._AddPosition('Auxiliary Crew', 'A', 'E4', self)


class DamageControlDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Damage Control Officer', 'A', 'O2', self)
        self._AddPosition('Damage Control Chief', 'A', 'N2', self)


class ImpellerDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Impeller Officer', 'A', 'O1', self)
        self._AddPosition('Impeller Chief', 'A', 'N2', self)
        for i in range(3):
            self._AddPosition('Impeller Crew', 'A', 'E4', self)


class ReactorDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Reactor Officer', 'A', 'O2', self)
        for i in range(2):
            self._AddPosition('Reactor Chief', 'A', 'N2', self)
            for j in range(3):
                self._AddPosition('Reactor Crew', 'A', 'E4', self)


class SailsDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Sails Officer', 'A', 'O2', self)
        self._AddPosition('Sails Chief', 'A', 'N2', self)
        for j in range(3):
            self._AddPosition('Sails Crew', 'A', 'E4', self)


class MissileDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Missile Officer', 'A', 'W1', self)
        self._AddPosition('Missile Chief', 'A', 'N2', self)
        for i in range(8):
            self._AddPosition('Tube Chief', 'A', 'N1', self)
            for j in range(2):
                self._AddPosition('Tube Crew', 'A', 'E4', self)


class OrdnanceDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Magazine Officer', 'A', 'W1', self)
        self._AddPosition('Magazine Chief', 'A', 'N2', self)
        for i in range(2):
            self._AddPosition('Bay Chief', 'A', 'N1', self)
            for j in range(2):
                self._AddPosition('Magazine Crew', 'A', 'E4', self)


class WeaponsDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Weapons Officer', 'A', 'W1', self)
        self._AddPosition('Weapons Chief', 'A', 'N2', self)
        for i in range(4):
            self._AddPosition('Gun Chief', 'A', 'N1', self)
            for j in range(2):
                self._AddPosition('Gun Crew', 'A', 'E4', self)


class SensorDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Sensor Officer', 'A', 'N2', self)
        self._AddPosition('Sensor Chief', 'A', 'N1', self)
        for i in range(2):
            self._AddPosition('Array Chief', 'A', 'N1', self)
            for j in range(3):
                self._AddPosition('Array Crewman', 'A', 'E4', self)


class SupplyAdminDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Admin Clerk', 'A', 'E4', self)


class FoodServiceDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Chief Steward', 'A', 'N1', self)
        for i in range(2):
            self._AddPosition("Steward's Mate", 'A', 'E4', self)
        self._AddPosition('Head Cook', 'A', 'N1', self)
        self._AddPosition('Cook', 'A', 'E4', self)
        for i in range(3):
            self._AddPosition('Mess Mate', 'A', 'E4', self)


class SalesServicesDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Store Manager', 'A', 'N1', self)
        for i in range(2):
            self._AddPosition('Store Clerk', 'A', 'E4', self)


class CargoDiv(Division):

    def _SetPositions(self):
        self._AddPosition('Bay Chief', 'A', 'N1', self)
        for i in range(2):
            self._AddPosition('Cargo Crewman', 'A', 'E4', self)


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

    def __init__(self, cmdUnit=None):
        Unit.__init__(self, cmdUnit)
        self._SetArsenal()

    def _SetSubUnits(self):
        self._SubUnits.append(AdminDept(self))
        self._SubUnits.append(TacticalDept(self))
        self._SubUnits.append(EngineeringDept(self))
        self._SubUnits.append(MedicalDept(self))
        self._SubUnits.append(OperationsDept(self))
        self._SubUnits.append(SupplyDept(self))
        self._SubUnits.append(SecurityDetachment(self))

    def _SetPositions(self):
        self._AddPosition('Commanding Officer', 'A', 'O4', self)
        self._AddPosition('Executive Officer', 'A', 'O3', self)
        self._AddPosition('Boatswain', 'A', 'N5', self)

    def _SetArsenal(self):
        self._Arsenal = {}
        self._Arsenal['Chase'] = {'Bow': [], 'Stern': []}
        self._Arsenal['Broadside'] = {'Port': [], 'Starboard': []}
        for i in range(3):
            self._Arsenal['Broadside']['Port'].append('Missile Tube')
            self._Arsenal['Broadside']['Starboard'].append('Missile Tube')
        self._Arsenal['Broadside']['Port'].append('Laser Mount')
        self._Arsenal['Broadside']['Starboard'].append('Laser Mount')
        self._Arsenal['Chase']['Bow'].append('Graser Mount')
        self._Arsenal['Chase']['Bow'].append('Missile Tube')
        self._Arsenal['Chase']['Stern'].append('Graser Mount')
        self._Arsenal['Chase']['Stern'].append('Missile Tube')

    def _SetSmallCraft(self):
        self._SmallCraft = ['Pinnace']
