from Imperium.Military.StructureClasses import Branch, RankCategory, Rank
from Imperium.Military.Navy.LAC.Wing import Wing

Branches = []
Branches.append(Branch('Admiralty'))
Branches.append(Branch('Legion'))

Categories = []
Categories.append(RankCategory('Officer', (0, 11), Branches))
Categories.append(RankCategory('Warrant Officer', (1, 5), Branches))
Categories.append(RankCategory('Non-Commissioned Officer', (1, 8),
	Branches))
Categories.append(RankCategory('Enlisted', (0, 5), Branches))

Ranks = []
Ranks.append(Rank('Cadet', 0, Branches[1:], Categories[0]))
Ranks.append(Rank('Second Lieutenant', 1, Branches[1:], Categories[0]))
Ranks.append(Rank('First Lieutenant', 2, Branches[1:], Categories[0]))
Ranks.append(Rank('Captain', 3, Branches[1:], Categories[0]))
Ranks.append(Rank('Major', 4, Branches[1:], Categories[0]))
Ranks.append(Rank('Lieutenant Colonel', 5, Branches[1:], Categories[0]))
Ranks.append(Rank('Colonel', 6, Branches[1:], Categories[0]))
Ranks.append(Rank('Brigadier', 7, Branches[1:], Categories[0]))
Ranks.append(Rank('Major General', 8, Branches[1:], Categories[0]))
Ranks.append(Rank('Lieutenant General', 9, Branches[1:], Categories[0]))
Ranks.append(Rank('General', 10, Branches[1:], Categories[0]))
Ranks.append(Rank('Field Marshal', 11, Branches[1:], Categories[0]))

Ranks.append(Rank('Midshipman', 0, Branches[0], Categories[0]))
Ranks.append(Rank('Ensign', 1, Branches[0], Categories[0]))
Ranks.append(Rank('Lieutenant Junior Grade', 2, Branches[0],
	Categories[0]))
Ranks.append(Rank('Lieutenant Senior Grade', 3, Branches[0],
	Categories[0]))
Ranks.append(Rank('Lieutenant Commander', 4, Branches[0],
	Categories[0]))
Ranks.append(Rank('Commander', 5, Branches[0], Categories[0]))
Ranks.append(Rank('Captain Junior Grade', 6, Branches[0],
	Categories[0], True, '-'))
Ranks.append(Rank('Captain Senior Grade', 6, Branches[0], Categories[0],
	True, '+'))
Ranks.append(Rank('Commodore', 7, Branches[0], Categories[0]))
Ranks.append(Rank('Rear Admiral of the Red', 8, Branches[0],
	Categories[0], True, '-'))
Ranks.append(Rank('Rear Admiral of the Green', 8, Branches[0],
	Categories[0], True, '+'))
Ranks.append(Rank('Vice Admiral of the Red', 9, Branches[0],
	Categories[0], True, '-'))
Ranks.append(Rank('Vice Admiral of the Green', 9, Branches[0],
	Categories[0], True, '+'))
Ranks.append(Rank('Admiral of the Red', 10, Branches[0], Categories[0],
	True, '-'))
Ranks.append(Rank('Admiral of the Green', 10, Branches[0],
	Categories[0], True, '+'))
Ranks.append(Rank('Fleet Admiral', 11, Branches[0], Categories[0]))

Ranks.append(Rank('Warrant Officer', 1, Branches, Categories[1]))
Ranks.append(Rank('Warrant Officer Third Class', 2, Branches, Categories[1]))
Ranks.append(Rank('Warrant Officer Second Class', 3, Branches, Categories[1]))
Ranks.append(Rank('Warrant Officer First Class', 4, Branches, Categories[1]))
Ranks.append(Rank('Chief Warrant Officer', 5, Branches, Categories[1]))

Ranks.append(Rank('Petty Officer Third Class', 1, Branches[0], Categories[2]))
Ranks.append(Rank('Petty Officer Second Class', 2, Branches[0], Categories[2]))
Ranks.append(Rank('Petty Officer First Class', 3, Branches[0], Categories[2]))
Ranks.append(Rank('Chief Petty Officer', 4, Branches[0], Categories[2]))
Ranks.append(Rank('Senior Chief Petty Officer', 5, Branches[0], Categories[2]))
Ranks.append(Rank('Master Chief Petty Officer', 6, Branches[0], Categories[2]))

Ranks.append(Rank('Corporal', 1, Branches[1:], Categories[2]))
Ranks.append(Rank('Sergeant', 2, Branches[1:], Categories[2]))
Ranks.append(Rank('Sergeant First Class', 3, Branches[1:], Categories[2]))
Ranks.append(Rank('Master Sergeant', 4, Branches[1:], Categories[2]))
Ranks.append(Rank('Sergeant Major', 5, Branches[1:], Categories[2]))
Ranks.append(Rank('Command Sergeant Major', 6, Branches[1:], Categories[2]))

Ranks.append(Rank('Legionaire Recruit', 0, Branches[1], Categories[3]))
Ranks.append(Rank('Legionaire', 1, Branches[1], Categories[3]))
Ranks.append(Rank('Legionaire Third Class', 2, Branches[1], Categories[3]))
Ranks.append(Rank('Legionaire Second Class', 3, Branches[1], Categories[3]))
Ranks.append(Rank('Legionaire First Class', 4, Branches[1], Categories[3]))
Ranks.append(Rank('Senior Legionaire', 5, Branches[1], Categories[3]))

Ranks.append(Rank('Crewman Recruit', 0, Branches[0], Categories[3]))
Ranks.append(Rank('Crewman', 1, Branches[0], Categories[3]))
Ranks.append(Rank('Crewman Third Class', 2, Branches[0], Categories[3]))
Ranks.append(Rank('Crewman Second Class', 3, Branches[0], Categories[3]))
Ranks.append(Rank('Crewman First Class', 4, Branches[0], Categories[3]))
Ranks.append(Rank('Senior Crewman', 5, Branches[0], Categories[3]))

testWing = Wing()
testWing.FillPositions()
