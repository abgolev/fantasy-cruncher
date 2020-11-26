import csv
import pandas as pd
import numpy as np

for y in range(1970, 2020):
	doc = r'data_v2/yearly/' + str(y) + '.csv'
	df = pd.read_csv(doc)
	rushYds = df.loc[:, 'RushingYds']
	recYds = df.loc[:, 'ReceivingYds']
	passYds = df.loc[:, 'PassingYds']
	rushTDs = df.loc[:, 'RushingTD']
	recTDs = df.loc[:, 'ReceivingTD']
	passTDs = df.loc[:, 'PassingTD']
	gamesPlayed = df.loc[:, 'G']
	completions = df.loc[:, 'Cmp']
	passAtt = df.loc[:, 'PassingAtt']
	rushAtt = df.loc[:, 'RushingAtt']
	receptions = df.loc[:, 'Rec']
	fumbles = df.loc[:, 'FumblesLost']
	interceptions = df.loc[:, 'Int']
	if y>=1992:
		targets = df.loc[:, 'Tgt']

	flexYds = []
	flexTDs = []
	avgPassYds = []
	avgRushYds = []
	avgRecYds = []
	avgFlexYds = []
	avgPassTDs = []
	avgRushTDs = []
	avgRecTDs = []
	avgFlexTDs = []
	cmpPercentage = []
	ydsPerPassCmp = []
	ydsPerPassAtt = []
	ydsPerRush = []
	avgRecs = []
	catchPercentage = []
	fantasyPts = []	
	avgFantasyPts = []
	tgt = []

	print("Length: "+str(len(rushYds)))
	
	for x in range(len(rushYds)):
		flexYds.append(int(rushYds[x]) + int(recYds[x]))
		flexTDs.append(rushTDs[x] + recTDs[x])
		if gamesPlayed[x] !=0 :
			avgPassYds.append(passYds[x]/gamesPlayed[x])
			avgRushYds.append(rushYds[x]/gamesPlayed[x])
			avgRecYds.append(recYds[x]/gamesPlayed[x])
			avgFlexYds.append(flexYds[x]/gamesPlayed[x])
			avgPassTDs.append(passTDs[x]/gamesPlayed[x])
			avgRushTDs.append(rushTDs[x]/gamesPlayed[x])
			avgRecTDs.append(recTDs[x]/gamesPlayed[x])
			avgFlexTDs.append(flexTDs[x]/gamesPlayed[x])
			avgRecs.append(receptions[x]/gamesPlayed[x])
		else:
			avgPassYds.append(0)
			avgRushYds.append(0)
			avgRecYds.append(0)
			avgFlexYds.append(0)
			avgPassTDs.append(0)
			avgRushTDs.append(0)
			avgRecTDs.append(0)
			avgFlexTDs.append(0)
			avgRecs.append(0)

		if y >= 1992:
			if targets[x] != 0:
				catchPercentage.append(receptions[x]/targets[x])					
			else:
				catchPercentage.append(0)	
		else:
			catchPercentage.append(0)
			tgt.append(0)

		if passAtt[x] != 0:
			cmpPercentage.append(completions[x]/passAtt[x])
			ydsPerPassAtt.append(passYds[x]/passAtt[x])
		else:
			cmpPercentage.append(0)
			ydsPerPassAtt.append(0)
			
		if completions[x] != 0:
			ydsPerPassCmp.append(passYds[x]/completions[x])
		else:
			ydsPerPassCmp.append(0)

		if rushAtt[x] != 0:
			ydsPerRush.append(rushYds[x]/rushAtt[x])			
		else:		
			ydsPerRush.append(0)			

		pointsMyLeague = passYds[x]/25 + rushYds[x]/10 + recYds[x]/10 + receptions[x]*0.5 + passTDs[x]*4 + rushTDs[x]*6 + recTDs[x]*6 - fumbles[x]*2 - interceptions[x]*2
		fantasyPts.append(pointsMyLeague)		

		if gamesPlayed[x] != 0:
			avgFantasyPts.append(fantasyPts[x]/gamesPlayed[x])
		else:
			avgFantasyPts.append(0)

	if y < 1992:
		df['Tgt'] = tgt
	df['FlexYds'] = flexYds
	df['FlexTDs'] = flexTDs
	df['avgPassYds'] = avgPassYds
	df['avgRushYds'] = avgRushYds
	df['avgRecYds'] = avgRecYds
	df['avgFlexYds'] = avgFlexYds
	df['avgPassTDs'] = avgPassTDs
	df['avgRushTDs'] = avgRushTDs
	df['avgRecTDs'] = avgRecTDs
	df['avgFlexTDs'] = avgFlexTDs
	df['ydsPerRushAtt'] = ydsPerRush
	df['cmpPercentage'] = cmpPercentage
	df['ydsPerPassCmp'] = ydsPerPassCmp
	df['ydsPerPassAtt'] = ydsPerPassAtt
	df['avgRecs'] = avgRecs 
	df['catchPercentage'] = catchPercentage 
	df['fantasyPts'] = fantasyPts 
	df['avgFantasyPts'] = avgFantasyPts

	df.to_csv(r'data_v2/yearly_updated/'+str(y)+'.csv', index=False)
	#df.to_csv(r'meowy.csv', index=False)
