import csv
import pandas as pd
import numpy as np
import tkinter as tk
import random
from sklearn.linear_model import LinearRegression

def computeFantasyPoints(df, rules):
	for i in range(0,len(df.index)):
		passYds = df['PassingYds'].values[i]
		rushYds = df['RushingYds'].values[i]
		recYds = df['ReceivingYds'].values[i]
		receptions = df['Rec'].values[i]
		passTDs = df['PassingTD'].values[i]
		rushTDs = df['RushingTD'].values[i]
		recTDs = df['ReceivingTD'].values[i]
		fumbles = df['FumblesLost'].values[i]
		interceptions = df['Int'].values[i]
		newPoints = passYds/rules[0] + rushYds/rules[1] + recYds/rules[2] + receptions*rules[3] + passTDs*rules[4] + rushTDs*rules[5] + recTDs*rules[6] + fumbles*rules[7] + interceptions*rules[8] 
		if df['G'].values[i] == 0:
			newAvgPoints = 0
		else:
			newAvgPoints = newPoints / df['G'].values[i]
		df.at[i, 'fantasyPts'] = newPoints
		df.at[i, 'avgFantasyPts'] = newAvgPoints
		
	return df

def selectColumnsLinReg(newd, d, d2, year, cols):
	for c in cols:
		a1 = d.loc[:, c]
		a2 = d2.loc[:, c]
		a1 = np.array(a1)
		a2 = np.array(a2)
		newd[c+str(year)] = a1
		newd[c+str(year+1)] = a2
	return newd

def FunFact():
	r = random.randrange(1, 46, 1)

	print("Fun Fact:")

	if r == 1:
		print("Frank Gore is made entirely of scrap metal and grit.")
	if r == 2:
		print("Frank Gore is made entirely of scrap metal and grit.")
	if r == 3:
		print("Frank Gore is made entirely of scrap metal and grit.")
	if r == 4:
		print("Frank Gore is made entirely of scrap metal and grit.")
	if r == 5:
		print("The cops who killed Breonna Taylor still haven't been arrested.")
	if r == 6:
		print("The inventor of the frisbee was cremated and made into a frisbee when he died.")
	if r == 7:
		print("Joe Rogan and Gerard Way are cousins.")
	if r == 8:
		print("Left handed people were once thought to be cursed. This is origin of the word 'sinister'.")
	if r == 9:
		print("Greenland is a territory of Denmark.")
	if r == 10:
		print("Eddie Izzard completed 27 marathons in 27 days at age 54.")
	if r == 11:
		print("Shaq made 11,330 shots in his career, out of which exactly 1 was a 3-pointer.")
	if r == 12:
		print("There are more trees on Earth than stars in the galaxy.")
	if r == 13:
		print("Time is an illusion, lunchtime doubly so.")
	if r == 14:
		print("In the beginning, the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.")
	if r == 15:
		print("Nothing travels faster than the speed of light with the possible exception of bad news, which obeys its own special laws.")
	if r == 16:
		print("The CPU in a TI-83 is the same as the one in a Gameboy.")
	if r == 17:
		print("Kansas is proportionally flatter than a pancake.")
	if r == 18:
		print("A group of pugs is called a grumble.")
	if r == 19:
		print("Just because you are a character doesn't mean you have character.")
	if r == 20:
		print("The Casa Bonita restaurant in Denver has a specialized system that monitors whenever the South Park Casa Bonita episode airs because that causes an influx of patrons over the course of the next week.")
	if r == 21:
		print("A perfect simulacrum hides the fact that there was no original to begin with.")
	if r == 22:
		print("What can be said at all can be said clearly, and what we cannot talk about we must pass over in silence.")
	if r == 23:
		print("The word 'beccles' refers to the small bone buttons placed in bacon sandwiches by unemployed guerrilla dentists.")
	if r == 24:
		print("John Tyler, 10th president of the United States, has two living grandchildren.")
	if r == 25:
		print("Before a Scottish Premier League soccer match, it was reported in the media that Rangers goalie Andy Goram had a mild form of schizophrenia. During the match, the Kilmanrock fans heckled him by singing 'Two Andy Gorams, there's only two Andy Gorams'")	
	if r == 26:
		print("There is code in this program specifically written to correctly match up the different Adrian Petersons and Steve Smithses.")
	if r == 27:
		print("In Bulgaria, shaking your head means yes and nodding means no.")
	if r == 28:
		print("Platypuses have poison in their ankles that can incapacitate a grown man.")
	if r == 29:
		print("Fantasy Football was invented in 1974 by George Fantasy.")
	if r == 30:
		print("In 2019, Tom Brady led the league with 2437 yards pacing around angrily on the sideline muttering mean things to himself.")
	if r == 31:
		print("Antonio Brown is currently scuba diving in the Newport Aquarium.")
	if r == 32:
		print("The cause behind the Amelia Earhart disappearance is now thought to be that her plane was struck by an errant Mitch Trubisky throw.")
	if r == 33:
		print("Antonio Brown is currently investigating the cause behind the Amelia Earhart disappearance.")
	if r == 34:
		print("Antonio Brown is currently doing hot yoga at a Wendy's.")
	if r == 35:
		print("A wise old man once told me, 'an albatross in the hand is worth dos in the moss'.")
	if r == 36:
		print("London beckons songs about money written by machines.")
	if r == 37:
		print("Antonio Brown is currently homebrewing kombucha.")
	if r == 38:
		print("Antonio Brown is currently executive producing a three-part Netflix miniseries on the bathing habits of Buddhist monks.")
	if r == 39:
		print("Antonio Brown is currently getting real big into steampunk.")
	if r == 40:
		print("Antonio Brown is currently participating in a competitive hopscotch league.")
	if r == 41:
		print("Antonio Brown is currently learning how to play the cello with his toes.")
	if r == 42:
		print("Antonio Brown is currently instructing a beginners' spelunking class.")
	if r == 43:
		print("Antonio Brown is currently doing a chaotic good playthrough of Madden 2013.")
	if r == 44:
		print("Antonio Brown is currently getting an earlobe massage from a Filipina fortuneteller.")
	if r == 45:
		print("Antonio Brown is currently yelling at a horse.")
	if r == 46:
		print("Antonio Brown is currently googling the answers to the online homework for his Advanced Principles of Astrology course.")

def sort(METRIC_TYPE, MIN_YEAR, MAX_YEAR, MIN_PASS, MIN_RUSH, MIN_REC, MIN_GAMES, MIN_POINTS_METRIC, POSITION, TEAM, MAX_PLAYERS, LEAGUE_RULES, OUTPUT_COLUMNS):

	for y in range(MIN_YEAR, MAX_YEAR+1):

		#doc = '' + str(y) + '.csv'
		doc = r'data_v2/yearly_updated/' + str(y) + '.csv'
		df1 = pd.read_csv(doc)

		computeFantasyPts = False

		for c in OUTPUT_COLUMNS:
			if c == 'fantasyPts' or c == 'avgFantasyPts':
				computeFantasyPts = True

		#Used for customized league rules
		if METRIC_TYPE == "fantasyPts" or METRIC_TYPE == "avgFantasyPts" or computeFantasyPts == True:
			df1 = computeFantasyPoints(df1, LEAGUE_RULES)

		for x in range(len(df1.index)-1, -1, -1):
			if df1[METRIC_TYPE].values[x] <= MIN_POINTS_METRIC or df1['G'].values[x] <= MIN_GAMES:
				df1 = df1.drop(df1.index[x])
			elif POSITION != "All" and POSITION != "FLEX" and df1['Pos'].values[x] != POSITION:				
				df1 = df1.drop(df1.index[x])
			elif POSITION == "FLEX" and df1['Pos'].values[x]!="RB" and df1['Pos'].values[x]!="WR" and df1['Pos'].values[x]!="TE":
				df1 = df1.drop(df1.index[x])
			elif TEAM != "All" and df1['Tm'].values[x] != TEAM:				
				df1 = df1.drop(df1.index[x])
			elif df1['PassingAtt'].values[x] < MIN_PASS or df1['RushingAtt'].values[x] < MIN_RUSH or df1['Rec'].values[x] < MIN_REC:
				df1 = df1.drop(df1.index[x])

		df1 = df1.sort_values(by=METRIC_TYPE, ascending=False)

		while len(df1.index) > MAX_PLAYERS:		
			df1 = df1.drop(df1.index[len(df1.index)-1])

		print("Year: " + str(y))

		pd.set_option('display.max_columns', 1000)
		pd.set_option('display.max_rows', 1000)
		pd.set_option('display.width', 10000)

		if len(df1.index) < 1:
			print("Search found no such values")

		else:
			if len(OUTPUT_COLUMNS) == 1 and OUTPUT_COLUMNS[0] == 'All':
				df1 = df1.sort_values(by=[METRIC_TYPE], ascending=False)
				column1 = df1.loc[:, 'Player']
				column2 = df1.loc[:, METRIC_TYPE]
				df1 = df1.drop(columns=METRIC_TYPE)
				df1 = df1.drop(columns='Player')
				df1.insert(1, 'Player', column1)
				df1.insert(2, METRIC_TYPE, column2)
				df1 = df1.drop(columns='Unnamed: 0')
				print(df1.to_string(index=False))
				df1.to_csv(r'__data_sort_'+METRIC_TYPE+'_'+str(y)+'.csv', index=False)
			else:
				col_names = []
				col_names.append('Player')		
				col_names.append(METRIC_TYPE)		
				for c in OUTPUT_COLUMNS:
					if c != METRIC_TYPE:
						col_names.append(c)

				newdf = df1[col_names]
				newdf = newdf.sort_values(by=[METRIC_TYPE], ascending=False)
				print(newdf.to_string(index=False))
				newdf.to_csv(r'__data_sort_'+METRIC_TYPE+'_'+str(y)+'.csv', index=False)

def lin_reg(METRIC_TYPE, MIN_YEAR, MAX_YEAR, MIN_PASS, MIN_RUSH, MIN_REC, MIN_GAMES, MIN_POINTS_METRIC, POSITION, TEAM, MAX_PLAYERS, LEAGUE_RULES, OUTPUT_COLUMNS):
	coefficient_array = [] #used to print average r-squared at the very end
	linear_equation_array = []
	coefficient_dict = {}

	for y in range(MIN_YEAR, MAX_YEAR):
		doc1 = r'data_v2/yearly_updated/' + str(y) + '.csv'
		doc2 = r'data_v2/yearly_updated/' + str(y+1) + '.csv' 
		#doc1 = r'' + str(y) + '.csv'
		#doc2 = r'' + str(y+1) + '.csv'		
		df1 = pd.read_csv(doc1)
		df2 = pd.read_csv(doc2)

		computeFantasyPts = False

		for c in OUTPUT_COLUMNS:
			if c == 'fantasyPts' or c == 'avgFantasyPts':
				computeFantasyPts = True

		#Used for customized league rules
		if METRIC_TYPE == "fantasyPts" or METRIC_TYPE == "avgFantasyPts" or computeFantasyPts == True:
			df1 = computeFantasyPoints(df1, LEAGUE_RULES)
			df2 = computeFantasyPoints(df2, LEAGUE_RULES)

		df1 = df1.sort_values(by=['Player', 'Tm'])
		df2 = df2.sort_values(by=['Player', 'Tm'])

		#Clean up data based on desired user input
		#for x in range(len(namesList1)-1, -1, -1):
		for x in range(len(df1.index)-1, -1, -1):
			if df1[METRIC_TYPE].values[x] <= MIN_POINTS_METRIC or df1['G'].values[x] <= MIN_GAMES:
				df1 = df1.drop(df1.index[x])
			elif POSITION != "All" and POSITION != "FLEX" and df1['Pos'].values[x] != POSITION:				
				df1 = df1.drop(df1.index[x])
			elif POSITION == "FLEX" and df1['Pos'].values[x]!="RB" and df1['Pos'].values[x]!="WR" and df1['Pos'].values[x]!="TE":
				df1 = df1.drop(df1.index[x])
			elif TEAM != "All" and df1['Tm'].values[x] != TEAM:				
				df1 = df1.drop(df1.index[x])
			elif df1['PassingAtt'].values[x] < MIN_PASS or df1['RushingAtt'].values[x] < MIN_RUSH or df1['Rec'].values[x] < MIN_REC:
				df1 = df1.drop(df1.index[x])

		for x in range(len(df2.index)-1, -1, -1):
			#if df2[METRIC_TYPE].values[x] <= MIN_POINTS_METRIC or df2['G'].values[x] <= MIN_GAMES:
			#	df2 = df2.drop(df2.index[x])
			if df2['G'].values[x] <= MIN_GAMES:
				df2 = df2.drop(df2.index[x])
			elif POSITION != "All" and POSITION != "FLEX" and df2['Pos'].values[x] != POSITION:				
				df2 = df2.drop(df2.index[x])
			elif POSITION == "FLEX" and df2['Pos'].values[x]!="RB" and df2['Pos'].values[x]!="WR" and df2['Pos'].values[x]!="TE":
				df2 = df2.drop(df2.index[x])
			elif TEAM != "All" and df2['Tm'].values[x] != TEAM:				
				df2 = df2.drop(df2.index[x])
			elif df2['PassingAtt'].values[x] < MIN_PASS or df2['RushingAtt'].values[x] < MIN_RUSH or df2['Rec'].values[x] < MIN_REC:
				df2 = df2.drop(df2.index[x])

		
		min_index = min(len(df1.index), len(df2.index))

		#Remove nonmatching names
		for x in range(min_index):
			if x>= len(df1.index) or x>= len(df2.index):
				break

			while df1['Player'].values[x] != df2['Player'].values[x]:
				if df1['Player'].values[x] < df2['Player'].values[x]:
					df1 = df1.drop(df1.index[x])
				elif df1['Player'].values[x] > df2['Player'].values[x]:
					df2 = df2.drop(df2.index[x])

				if x>= len(df1.index) or x>= len(df2.index):
					break

		#If one list is longer, remove leftover entries
		if len(df1.index) > len(df2.index):
			while len(df1.index) > len(df2.index):
				df1 = df1.drop(df1.index[len(df1.index)-1])
		elif len(df1.index) < len(df2.index):
			while len(df1.index) < len(df2.index):
				df2 = df2.drop(df2.index[len(df2.index)-1])


		#Delete multiple Mike Williamses and Steve Smithses and Adrian Petersons on different teams, just in case
		for x in range(len(df1.index)):
			if x >= len(df1.index) or x >= len(df2.index):
				break

			if df1['Player'].values[x] == "Steve Smith" or df1['Player'].values[x] == "Adrian Peterson" or df1['Player'].values[x] == "Mike Williams":
				if  df1['Tm'].values[x]!= df2['Tm'].values[x]:
					df1 = df1.drop(df1.index[x])
					df2 = df2.drop(df2.index[x])

		df1 = df1.sort_values(by=METRIC_TYPE, ascending=False)

		#Editing for Max Players
		while len(df1.index) > MAX_PLAYERS:		
			df1 = df1.drop(df1.index[len(df1.index)-1])
		df1 = df1.sort_values(by='Player')
		for x in range(len(df1.index)):
			while df1['Player'].values[x] != df2['Player'].values[x]:
				df2 = df2.drop(df2.index[x])
		while len(df2.index) > MAX_PLAYERS:		
			df2 = df2.drop(df2.index[len(df2.index)-1])

		print("Year: " + str(y))

		if len(df1.index) < 2:
			print("No such data found. Double check your customizable variables values.")
		else:

			#For printing column output

			newdf = pd.DataFrame() 

			names1 = df1.loc[:, 'Player']
			names2 = df2.loc[:, 'Player']
			metric1 = df1.loc[:, METRIC_TYPE]
			metric2 = df2.loc[:, METRIC_TYPE]

			names1=np.array(names1)
			metric1=np.array(metric1)
			metric2=np.array(metric2)

			newdf['Player'] = names1
			newdf[METRIC_TYPE+str(y)] = metric1
			newdf[METRIC_TYPE+str(y+1)] = metric2

			if len(OUTPUT_COLUMNS)==1 and OUTPUT_COLUMNS[0] == 'All':
				for col in df1.columns:
					if col != 'Player' and col!= 'Unnamed: 0':
						x1 = df1.loc[:, col]
						x2 = df2.loc[:, col]
						x1 = np.array(x1)
						x2 = np.array(x2)
						newdf[col+str(y)] = x1
						newdf[col+str(y+1)] = x2
			else:
				selectColumnsLinReg(newdf, df1, df2, y, OUTPUT_COLUMNS)

			pd.set_option('display.max_columns', 1000)
			pd.set_option('display.max_rows', 1000)
			pd.set_option('display.width', 10000)
	
			newdf = newdf.sort_values(by=[METRIC_TYPE+str(y)], ascending=False)
			print(newdf.to_string(index=False))

			newdf.to_csv(r'__data_LinReg_'+METRIC_TYPE+'_'+str(y)+'.csv', index=False)

			#Linear Regression
			x1 = np.array(metric1)
			x1 = x1.reshape(-1,1)
			y1 = np.array(metric2)


			model = LinearRegression().fit(x1,y1)
			r_sq = model.score(x1,y1)
		#	print('coefficient of determination:', r_sq)
			coefficient_array.append(r_sq)
			coefficient_dict[y] = round(r_sq,3)
		#	print('intercept:', model.intercept_)
		#	print('slope:', model.coef_)
			lin_reg = "Regression equation for " + str(y) + ": " + "y="+str(round(model.coef_[0],3))+"x"+"+"+str(round(model.intercept_,3))
			linear_equation_array.append(lin_reg)
			
			print("Regression equation for " + str(y) + ": " + "y="+str(round(model.coef_[0],3))+"x"+"+"+str(round(model.intercept_,3)))

	print("")
	print("")
	print("Linear Regression Results:")
	sum = 0
	for x in range(len(coefficient_array)):
		sum+=coefficient_array[x]
	for x in range(len(linear_equation_array)):
		print(linear_equation_array[x])
	if len(coefficient_array) != 0:
		print("R-squared for each year:")
		for x in coefficient_dict:
			print(""+str(x)+": "+str(coefficient_dict[x]))
		#print(coefficient_dict)
		print("Average r-squared: "+str(round(sum/len(coefficient_array),3)))

doc = r'data_v2/yearly/2019.csv'
#doc = r'2019old.csv'
df = pd.read_csv(doc)

def start():
	metric_dropdown_type = metricDropdown.get()

	if metric_dropdown_type == "Fantasy Points":
		m_type = "fantasyPts"
	elif metric_dropdown_type == "Fantasy Points per game":
		m_type = "avgFantasyPts"
	elif metric_dropdown_type == "Pass yards":
		m_type = "PassingYds"
	elif metric_dropdown_type == "Rush yards":
		m_type = "RushingYds"
	elif metric_dropdown_type == "Receiving yards":
		m_type = "ReceivingYds"
	elif metric_dropdown_type == "FLEX yards":
		m_type = "FlexYds"
	elif metric_dropdown_type == "Pass yards per game":
		m_type = "avgPassYds"
	elif metric_dropdown_type == "Rush yards per game":
		m_type = "avgRushYds"
	elif metric_dropdown_type == "Receiving yards per game":
		m_type = "avgRecYds"
	elif metric_dropdown_type == "FLEX yards per game":
		m_type = "avgFlexYds"
	elif metric_dropdown_type == "Pass TDs":
		m_type = "PassingTD"
	elif metric_dropdown_type == "Rush TDs":
		m_type = "RushingTD"
	elif metric_dropdown_type == "Receiving TDs":
		m_type = "ReceivingTD"
	elif metric_dropdown_type == "FLEX TDs":
		m_type = "FlexTDs"
	elif metric_dropdown_type == "Pass TDs per game":
		m_type = "avgPassTDs"
	elif metric_dropdown_type == "Rush TDs per game":
		m_type = "avgRushTDs"
	elif metric_dropdown_type == "Receiving TDs per game":
		m_type = "avgRecTDs"
	elif metric_dropdown_type == "FLEX TDs per game":
		m_type = "avgFlexTDs"
	elif metric_dropdown_type == "Pass completion %":
		m_type = "cmpPercentage"
	elif metric_dropdown_type == "Catch rate (only available 1992 and later)":
		m_type =  "catchPercentage"
	elif metric_dropdown_type == "Pass yards per attempt":
		m_type = "ydsPerPassAtt"
	elif metric_dropdown_type == "Rush yards per attempt":
		m_type = "ydsPerRushAtt"
	elif metric_dropdown_type == "Receptions":
		m_type = "Rec"
	elif metric_dropdown_type == "Targets (only available 1992 and later)":
		m_type = "Tgt"
	elif metric_dropdown_type == "Receptions per game":
		m_type = "avgRecs"
#	elif metric_dropdown_type == "Receiving yards per catch":
#		m_type = "Y/R"
	elif metric_dropdown_type == "Games played":
		m_type = "G"

	min_yr = int(minYearDropdown.get())
	max_yr = int(maxYearDropdown.get())
	min_g = float(eMinGames.get())
	min_metric = float(eMinMetric.get())
	min_pass = int(eMinPass.get())
	min_rush = int(eMinRush.get())
	min_rec = int(eMinRec.get())
	pos = positionDropdown.get()
	tm = teamDropdown.get()
	max_players = int(eMaxPlayers.get())

	league_rules = []
	league_rules.append(float(ePassYardsPerPoint.get()))
	league_rules.append(float(eRushYardsPerPoint.get()))
	league_rules.append(float(eRecYardsPerPoint.get()))
	league_rules.append(float(ePPR.get()))
	league_rules.append(float(ePointsPerPassTD.get()))
	league_rules.append(float(ePointsPerRushTD.get()))
	league_rules.append(float(ePointsPerRecTD.get()))
	league_rules.append(float(ePointsPerFumble.get()))
	league_rules.append(float(ePointsPerInt.get()))

	columns_for_output = []
	if(checkboxAllStats.get()==1):
		columns_for_output.append('All')
	else:
		if(checkboxGames.get()==1):
			columns_for_output.append('G')
		if(checkboxTeam.get()==1):
			columns_for_output.append('Tm')
		if(checkboxFantasyPts.get()==1):
			columns_for_output.append('fantasyPts')
		if(checkboxAvgFantasyPts.get()==1):
			columns_for_output.append('avgFantasyPts')
		if(checkboxPassing.get()==1):
			columns_for_output.append('Cmp')
			columns_for_output.append('Att')
			columns_for_output.append('Yds')
			columns_for_output.append('Int')
			columns_for_output.append('PassingTD')
			columns_for_output.append('avgPassYds')
			columns_for_output.append('avgPassTDs')
			columns_for_output.append('cmpPercentage')
			columns_for_output.append('ydsPerPassCmp')
			columns_for_output.append('ydsPerPassAtt')
		if(checkboxRushing.get()==1):
			columns_for_output.append('RushingYds')
			columns_for_output.append('RushingTD')
			columns_for_output.append('RushingAtt')
			columns_for_output.append('avgRushYds')
			columns_for_output.append('avgRushTDs')
			columns_for_output.append('ydsPerRushAtt')
		if(checkboxReceiving.get()==1):
			columns_for_output.append('Tgt')
			columns_for_output.append('Rec')
			columns_for_output.append('Y/R')
			columns_for_output.append('ReceivingYds')
			columns_for_output.append('ReceivingTD')
			columns_for_output.append('avgRecYds')
			columns_for_output.append('avgRecTDs')
			columns_for_output.append('avgRecs')
			#columns_for_output.append('avgcatchPercentage')
		if(checkboxFlexYds.get()==1):
			columns_for_output.append('FlexYds')
		if(checkboxFlexTDs.get()==1):
			columns_for_output.append('FlexTDs')
		if(checkboxAvgFlexYds.get()==1):
			columns_for_output.append('avgFlexYds')
		if(checkboxAvgFlexTDs.get()==1):
			columns_for_output.append('avgFlexTDs')

	function_type = functionDropdown.get()
	
	if(function_type=="Fun Fact"):
		FunFact()
	elif (m_type=="Tgt" or m_type=="catchPercentage") and min_yr<1992:
		print("No target data available before 1992. Enter a minimum year value greater than 1992.")
	elif(function_type=="Linear Regression" and min_yr >= max_yr):
		print("The Max Year must be greater than the Min Year for a linear regression.")
	elif(function_type=="Linear Regression"):
		lin_reg(m_type, min_yr, max_yr, min_pass, min_rush, min_rec, min_g, min_metric, pos, tm, max_players, league_rules, columns_for_output)
	elif(function_type=="Sort by Metric"):
		sort(m_type, min_yr, max_yr, min_pass, min_rush, min_rec, min_g, min_metric, pos, tm, max_players, league_rules, columns_for_output)
	

def exit():
	print("bye meow")
	window.destroy()

window = tk.Tk()

f1 = tk.Frame(window)

l1 = tk.Label(window, text="CUSTOMIZABLE VALUES:").grid(row=0, column=0)

l2 = tk.Label(window, text="Min metric score:").grid(row=1, column=0)
eMinMetric = tk.Entry(window, width=10)
eMinMetric.insert(0, "0")
eMinMetric.grid(row=1, column=1)

l3 = tk.Label(window, text="Min games played:").grid(row=2, column=0)
eMinGames = tk.Entry(window, width=10)
eMinGames.insert(0, "5")
eMinGames.grid(row=2, column=1)

l4 = tk.Label(window, text="Max players included:").grid(row=3, column=0)
eMaxPlayers = tk.Entry(window, width=10)
eMaxPlayers.insert(0, "1000") 
eMaxPlayers.grid(row=3, column=1)

new_l1 = tk.Label(window, text="Min pass attempts:").grid(row=4, column=0)
eMinPass = tk.Entry(window, width=10)
eMinPass.insert(0, "0") 
eMinPass.grid(row=4, column=1)

new_l2 = tk.Label(window, text="Min rush attempts:").grid(row=5, column=0)
eMinRush = tk.Entry(window, width=10)
eMinRush.insert(0, "0") 
eMinRush.grid(row=5, column=1)

new_l3 = tk.Label(window, text="Min receptions:").grid(row=6, column=0)
eMinRec = tk.Entry(window, width=10)
eMinRec.insert(0, "0") 
eMinRec.grid(row=6, column=1)

l5 = tk.Label(window, text="CUSTOMIZABLE LEAGUE RULES:").grid(row=7, column=0)

l6 = tk.Label(window, text="Passing yards per point:").grid(row=8, column=0)
ePassYardsPerPoint = tk.Entry(window, width=10)
ePassYardsPerPoint.insert(0, "25") 
ePassYardsPerPoint.grid(row=8, column=1)

l7 = tk.Label(window, text="Rushing yards per point:").grid(row=9, column=0)
eRushYardsPerPoint = tk.Entry(window, width=10)
eRushYardsPerPoint.insert(0, "10") 
eRushYardsPerPoint.grid(row=9, column=1)

l8 = tk.Label(window, text="Receiving yards per point:").grid(row=10, column=0)
eRecYardsPerPoint = tk.Entry(window, width=10)
eRecYardsPerPoint.insert(0, "10") 
eRecYardsPerPoint.grid(row=10, column=1)

l9 = tk.Label(window, text="Points per pass TD:").grid(row=11, column=0)
ePointsPerPassTD = tk.Entry(window, width=10)
ePointsPerPassTD.insert(0, "4") 
ePointsPerPassTD.grid(row=11, column=1)

l10 = tk.Label(window, text="Points per rush RD:").grid(row=12, column=0)
ePointsPerRushTD = tk.Entry(window, width=10)
ePointsPerRushTD.insert(0, "6") 
ePointsPerRushTD.grid(row=12, column=1)

l11 = tk.Label(window, text="Points per receiving TD:").grid(row=13, column=0)
ePointsPerRecTD = tk.Entry(window, width=10)
ePointsPerRecTD.insert(0, "6") 
ePointsPerRecTD.grid(row=13, column=1)

l12 = tk.Label(window, text="PPR:").grid(row=14, column=0)
ePPR = tk.Entry(window, width=10)
ePPR.insert(0, "0.5") 
ePPR.grid(row=14, column=1)

l13 = tk.Label(window, text="Points lost per fumble:").grid(row=15, column=0)
ePointsPerFumble = tk.Entry(window, width=10)
ePointsPerFumble.insert(0, "-2") 
ePointsPerFumble.grid(row=15, column=1)

l14 = tk.Label(window, text="Points lost per INT:").grid(row=16, column=0)
ePointsPerInt = tk.Entry(window, width=10)
ePointsPerInt.insert(0, "-2") 
ePointsPerInt.grid(row=16, column=1)

l15 = tk.Label(window, text="CHOOSE METRIC:", width=40) 
MetricList = ["Fantasy Points", "Fantasy Points per game","Pass yards", "Rush yards", "Receiving yards", "FLEX yards",
"Pass yards per game", "Rush yards per game", "Receiving yards per game", "FLEX yards per game",
"Pass TDs", "Rush TDs", "Receiving TDs", "FLEX TDs", 
"Pass TDs per game", "Rush TDs per game", "Receiving TDs per game", "FLEX TDs per game",
"Pass completion %", "Pass yards per attempt", "Rush yards per attempt",
"Receptions", "Catch rate (only available 1992 and later)",  "Targets (only available 1992 and later)", "Receptions per game", "Games played"]
metricDropdown = tk.StringVar(window)
metricDropdown.set(MetricList[0])
optMetric = tk.OptionMenu(window, metricDropdown, *MetricList)
l15.grid(row=0, column=2)
optMetric.grid(row=1, column=2)

l16 = tk.Label(window, text="CHOOSE FUNCTION:")
FunctionList = ["Linear Regression", "Sort by Metric", "Fun Fact"]
functionDropdown = tk.StringVar(window)
functionDropdown.set(FunctionList[0])
optFunction = tk.OptionMenu(window, functionDropdown, *FunctionList)
l16.grid(row=2, column=2)
optFunction.grid(row=3, column=2)

yearList=[]
for x in range(2019,1969,-1):
	yearList.append(x)

l17 = tk.Label(window, text="MIN YEAR:")
l17.grid(row=4, column=2)
minYearDropdown = tk.IntVar(window)
minYearDropdown.set(2018)
optMinYear = tk.OptionMenu(window, minYearDropdown, *yearList)
optMinYear.grid(row=5, column=2)

l18 = tk.Label(window, text="MAX YEAR:")
l18.grid(row=6, column=2)
maxYearDropdown = tk.IntVar(window)
maxYearDropdown.set(2019)
optMaxYear = tk.OptionMenu(window, maxYearDropdown, *yearList)
optMaxYear.grid(row=7, column=2)

positionList = ["All", "QB", "RB", "WR", "TE", "FLEX"]
l19 = tk.Label(window, text="Player Position:")
l19.grid(row=8, column=2)
positionDropdown = tk.StringVar(window)
positionDropdown.set("All")
optPosition = tk.OptionMenu(window, positionDropdown, *positionList)
optPosition.grid(row=9, column=2)

teamList = df['Tm'].unique() 
teamList.sort()
teamList = np.delete(teamList, [0,1], None)
teamList = np.insert(teamList, 0, "All", None)
l20 = tk.Label(window, text="Team:")
l20.grid(row=10, column=2)
teamDropdown = tk.StringVar(window)
teamDropdown.set(teamList[0])
optTeam = tk.OptionMenu(window, teamDropdown, *teamList)
optTeam.grid(row=11, column=2)

bStart = tk.Button(window, text = "START", command = start)
bStart.grid(row=20, column=3)

bExit = tk.Button(window, text = "EXIT", command = exit)
bExit.grid(row=21, column=3)

l21 = tk.Label(window, text="Additional data columns to output:")
l21.grid(row=0, column=3)
checkboxAllStats = tk.IntVar(window)
cb1 = tk.Checkbutton(window, text="All Stats", variable=checkboxAllStats)
checkboxPassing = tk.IntVar(window)
cb2 = tk.Checkbutton(window, text="All Passing Stats", variable=checkboxPassing)
checkboxRushing = tk.IntVar(window)
cb3 = tk.Checkbutton(window, text="All Rushing Stats", variable=checkboxRushing)
checkboxReceiving = tk.IntVar(window)
cb4 = tk.Checkbutton(window, text="All Receiving Stats", variable=checkboxReceiving)
checkboxFlexYds = tk.IntVar(window)
cb5 = tk.Checkbutton(window, text="Flex Yards", variable=checkboxFlexYds)
checkboxFlexTDs = tk.IntVar(window)
cb6 = tk.Checkbutton(window, text="Flex TDs", variable=checkboxFlexTDs)
checkboxAvgFlexYds = tk.IntVar(window)
cb7 = tk.Checkbutton(window, text="Avg Flex Yards", variable=checkboxAvgFlexYds)
checkboxAvgFlexTDs = tk.IntVar(window)
cb8 = tk.Checkbutton(window, text="Avg Flex TDs", variable=checkboxAvgFlexTDs)
checkboxGames = tk.IntVar(window)
cb9 = tk.Checkbutton(window, text="Games Played", variable=checkboxGames)
checkboxTeam = tk.IntVar(window)
cb10 = tk.Checkbutton(window, text="Team", variable=checkboxTeam)
checkboxFantasyPts = tk.IntVar(window)
cb11 = tk.Checkbutton(window, text="Fantasy Points", variable=checkboxFantasyPts)
checkboxAvgFantasyPts = tk.IntVar(window)
cb12 = tk.Checkbutton(window, text="Avg Fantasy Points", variable=checkboxAvgFantasyPts)
cb1.grid(row=1, column=3)
cb2.grid(row=2, column=3)
cb3.grid(row=3, column=3)
cb4.grid(row=4, column=3)
cb5.grid(row=5, column=3)
cb6.grid(row=6, column=3)
cb7.grid(row=7, column=3)
cb8.grid(row=8, column=3)
cb9.grid(row=9, column=3)
cb10.grid(row=10, column=3)
cb11.grid(row=11, column=3)
cb12.grid(row=12, column=3)

f1.grid(row=21, column=4)


window.mainloop()

