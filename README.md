# python-fundamentals1
This repo demonstrates my understanding of fundamental concepts in python such as menus and input validation.

A nerd is a person seen as overly intellectual, obsessive, introverted or lacking social skills. To check if a person is nerd or not, you can examine many aspects of this person. A program is created that allows individuals to calculate their 'nerd skill level'. The higher the skill level, the more powerful the nerd. This level is calculated using a special formula found in the subsequent sections. I have implemented a menu to allow the program to be used, an equation which can be used to calculate the score, and a printout
that allows a summation of the results.


The Menu

This menu is the main point of interaction between the user and the program. After each option is chosen, the program returns to the menu, so the user can select another option. The menu must have the following options:

1.) Enter Fandom Score
	i.) A person's "Fandom Score" is the number of things that the person considers themself a "fan of". For example, if a person likes
	both Star Wars and Star Trek but nothing else, then they have a score of 2.
	ii.) Note that a Fandom Score must be non-zero and non-negative. If a person enters a bad number the program should output an error
	message, but continue to run.

2.) Enter Hobbies Score
	i.) A person’s ‘Hobbies Score’ is the number of hobbies a person undertakes on a weekly basis. For example, if a person plays
	Fortnite, sews, dances, and swims every week, then they have a Hobbies Score of 16 (4 x 4) as we assume that one month contains 4
	weeks.
	ii.) Note that a Hobbies Score must be multiples of 4. Once the input is not valid, an error message must be displayed.
	iii.) Further, 0 is the multiple of 4.
	
3.) Enter Number of Sports played
	i.) A person is considered to play a sport if they own an item that could be used in that sport. If a person owns a soccer ball then
	their score is 1. If an item can be used for multiple sports, then it only counts as 1 towards this number.
	ii.) This score must be positive. Once again, error messages should appear if it is entered as negative.
	
4.) Calculate Nerd Score
	i,) This menu option will calculate the person’s Nerd Score. The score should be printed to the screen when calculated. The score is
	calculated using Figure 1.
	ii.) If any of the numbers above are not entered, then this option should display an error telling the user what it is missing.

5.) Print Nerd Rating of Students
	i.) Display the results of Nerd Class of a list of students. The class is determined in 'Finding Your Class' section
	

Implementing Nerd Score

x * sqrt(42*y^2 / z+1)

Where x = Fandom Score,
y = Hobbies Score,
z = Number of Sports Played

After obtaining the input value from the menu, the required variables are stored the appropriately and place the equation in the menu. The user should be able to get their Nerd Score, change one of the variables, and then recalculate to get the new value. For the sake of testing, use Table 1 below.

x 	y 	z 	Nerd score
1 	4 	1 	18.33030277982336
20 	4 	1 	366.6060555964672
20 	20 	1 	1833.030277982336
1 	20 	1 	91.6515138991168
1 	4 	50 	3.6299408518921203


Finding your Class

The numbers that come from the equation are mostly useless except for bragging rights. The program should output the person’s Nerd Class
which is determined by the score. Once a score surpasses a classes threshold, then they are considered to be a part of that class. For example, if the author of this paper received a score of 98.0, then he would be classed as a “Nerdlinger”. However if the author received a score of 100.0, then he would be classed as a “Nerd”.
Score 	Class 				Position in the output list
0 			Nerdlite 			0
1 			Nerdling 			1
10 			Nerdlinger 		2
100 		Nerd 					3
500 		Nerdington 		4
1000 		Nerdrometa 		5
2000 		Nerd Supreme 	6

Table 2: Score thresholds and their associated Class.

Given several students’ score (stored in a list), I hope to output the detailed numbers of each nerd class (stored in a list) defined in Table 2. Each index of the output list represent different class as mentioned in Table 2, e.g., the number of students who
are categorized as “Nerdlite” lies in the first item of the output list, i.e., the index of "Nerdlite" in the output list as 0. One test case is that given a list of nerd score [23, 76, 1300, 600], my program should output a list [0, 0, 2, 0, 1, 1, 0]. This list signifies that there are:
• 0 Nerdlite
• 0 Nerdling
• 2 Nerdlinger
• 0 Nerd
• 1 Nerdington
• 1 Nerdrometa
• 0 Nerd Supreme
