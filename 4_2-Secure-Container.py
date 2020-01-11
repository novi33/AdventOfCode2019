#! python3
# 
# Advent of Code Day IV
# Pt.2 Secure Container 
# Key facts about the password:
#				It is a six-digit number.
#				The value is within the range given in your puzzle input.
#				Two adjacent digits are the same (like 22 in 122345).
#				Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
#				*NEW fact - multiple same numbers no longer apply - at leaste one is two adjacent only!
# input: 271973-78596


passwordStarts = 271973
passwordEnds = 785961
numberOfHits = 0
countNumbers = {}
countNumbersList = []

for password in range(passwordStarts, (passwordEnds +1)):
	passwordString = str(password)
	countNumbers.clear()
	countNumbersList.clear()
	if ((passwordString[0] <= passwordString[1]) and (passwordString[1] <= passwordString[2]) and (passwordString[2] <= passwordString[3]) and 
		(passwordString[3] <= passwordString[4]) and (passwordString[4] <= passwordString[5])):
		# TODO find if there are two adjecent digits in the string; convert string to dictionary; count numbers (as keys) and sort them; second one should be 1 and first more then 1
		for i in passwordString:
			countNumbers[i] = countNumbers.get(i, 0)+1
		countNumbersList = list(sorted(countNumbers.items(), key=lambda x: x[1], reverse=True)) #reduce list and leave only list of number or even a string
		if any(2 in sublist for sublist in countNumbersList):
			numberOfHits += 1
			
print('Number of possible passwords: ' + str(numberOfHits))

