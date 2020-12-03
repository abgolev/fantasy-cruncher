# fantasy-cruncher
A tool for linear regressions, searches, and sorts on Fantasy Football data

Fantasy Cruncher takes custom input and runs it on data from 1970-2019 imported directly from Fantasy Football Data Pros. Output is printed to the terminal as well as saved as a new .csv file in the working directory. Below are a screenshot of the GUI and explanations of the different customizable options.

## Customizable Values:
### Min metric score:
The minimum cutoff for the metric selected in "Choose Metric" in the second column. For linear regressions, this minimum cutoff is limited to first season of the regression.
### Min games played:
Cutoff for minimum games the player took part in for the given season. For linear regressions, this is only limited the first season.
### Max players included:
After sorting the players based on the metric, only includes the top number of players specified.
### Min attemps/receptions:
Only includes players meeting this threshold.
### Customizable league rules:
If the metric selected is **Fantasy Points** or **Avg Fantasy Points**, recomputes the players' points based on the values selected in this section.

## Choose Metric:
Selects the category on which to base the linear regression or sort.
### Choose Function:
Linear regression runs on the metric selected for every pair of subsequent year in the range provided in the below categories. Sort function gives the top players in the given metric during each year.
### Min and Max Year:
Linear regression requires that the min year be earlier than the max year. For sorts, the same min year and max year can be used if the desired query is on one season only. The metrics Targets and Catch Rates are available in the original data only for years 1992 and later.
### Player Position and Team:
Positions limited to QB, RB, WR, TE, and FLEX. Flex includes the RB, WR, and TE categories.

## Additional output columns:

Default columns included in the output are the player name and metric. Any additional columns to be included have to be selected here.

**All Stats** overrides all other checkmarks and prints all columns included in the raw data, as well as additional columns derived by the raw data.

**All Passing Stats**, **All Rushing Stats**, and **All Receiving Stats** output a compilation of different categories related to that query.

**Fantasy Points** and **Avg Fantasy Points** are calculated using the input into the Customizable League Rules boxes in the first column.
