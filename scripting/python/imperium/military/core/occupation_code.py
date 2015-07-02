'''
S1 - Ops Officer - Battalion+
S2 - Intel Officer - Battalion+

S5 - Admin Officer - Battalion+
S6 - Logistic Officer - Battalion+
S7 - Communications Officer - Brigade+


MOS structure
RankCategory (First Digit) - Enlisted/NCO - blank, Officer/Warrant 1
MOS Branch (Second Digit) - Infantry 1, Armor 3, Artillery 4, Support 0
Organization Control (Third digit) Ops, Intel, etc
MOS Grouping - (Fourth digit) Different for different branch/control
Letter - MOS designator (Alphabet)
  - A-P - Enlisted, Low NCO 1-2
  - Q-W - Mid NCO 3-5
  - X - Training
  - Y - Open
  - Z - Senior NCO
'''

class MOSGroup(ImpObject, Branched):    
    pass

MOSGroups = []
MOSGroups.append(MOSGroup('111', 'C', 'Infantry'))
MOSGroups.append(MOSGroup('112', 'C','Basic Recon'))
MOSgroups.append(MOSGroup('059', 'C', 'Unit Administration'))
MOSgroups.append(MOSGroup('069', 'C', 'Unit Logistics'))
MOSgroups.append(MOSGroup('889', 'C', 'Combat Medicine'))

class MOS(ImpObject, Branched, Ranked):
    pass

MOSs = []
MOSs.append(MOS('111A', 'Rifleman', ['N', 'E'], [[1, 2], [1, 5]]))
MOSs.append(MOS('111C', 'Mortarman', ['N', 'E'], [[1, 2], [1, 5]]))
MOSs.append(MOS('111D', 'Plasma Gunner', ['N', 'E'], [[1, 2], [1, 5]]))
MOSs.append(MOS('111F', 'Missileman', ['N', 'E'], [[1, 2], [1, 5]]))
MOSs.append(MOS('112A', 'Scout', ['N', 'E'], [[1, 2], [1, 5]]
MOSs.append(MOS('112B', 'Scout Sniper', ['N', 'E']))
MOSs.append(MOS('111T', 'Unit Leader', 'N', [1, 4])) Squad/Section Leader, Platoon NCO
MOSs.append(MOS('111U', 'First Sergeant', 'N', [3, 5])) Company First Sergeant
MOSs.append(MOS('059F', 'Unit Clerk', ['N', 'E'], [1, 3], 5))
MOSs.append(MOS('069A', 'Unit Quartermaster', ['N', 'E'], [1, 3], 5))
MOSs.append(MOS('069D', 'Unit Armorer', ['N', 'E'], [1, 3], 5)) 
MOSs.append(MOS('889A', 'Combat Medic', 'E', [1, 5]))
MOSs.append(MOS('1111A', 'Infantry Officer', 'O', [1, 6]))
