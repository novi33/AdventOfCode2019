#! python3
# Run a string of integer and calculate - detail instructions are at https://adventofcode.com/2019/day/5
# expanded code and parameters:
# example, consider the program 1002,4,3,4,33:
#				ABCDE
#				 1002
#
#				DE - two-digit opcode,      02 == opcode 2
#				 C - mode of 1st parameter,  0 == position mode 
#				 B - mode of 2nd parameter,  1 == immediate mode (value in cell) *NEW
#				 A - mode of 3rd parameter,  0 == position mode,
#												  omitted due to being a leading zero		

import logging

opcode = [	3,225,1,225,6,6,1100,1,238,225,104,0,1102,17,65,225,102,21,95,224,1001,224,-1869,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,101,43,14,224,
			1001,224,-108,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,57,94,225,1101,57,67,225,1,217,66,224,101,-141,224,224,4,224,102,8,223,223,
			1001,224,1,224,1,224,223,223,1102,64,34,225,1101,89,59,225,1102,58,94,225,1002,125,27,224,101,-2106,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,
			223,223,1102,78,65,225,1001,91,63,224,101,-127,224,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1102,7,19,224,1001,224,-133,224,4,224,102,8,
			223,223,101,6,224,224,1,224,223,223,2,61,100,224,101,-5358,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,19,55,224,101,-74,224,224,4,
			224,102,8,223,223,1001,224,1,224,1,224,223,223,1101,74,68,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,
			227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,
			1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,677,677,224,102,2,223,223,1006,224,329,
			1001,223,1,223,1008,226,677,224,102,2,223,223,1006,224,344,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,8,226,226,224,102,2,
			223,223,1006,224,374,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,
			1108,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,434,101,1,223,223,1108,677,677,224,1002,223,2,223,
			1005,224,449,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,479,101,1,223,223,108,677,
			677,224,1002,223,2,223,1005,224,494,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,524,
			1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,554,1001,223,1,223,8,226,677,224,1002,
			223,2,223,1006,224,569,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,584,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,599,101,1,223,
			223,7,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,108,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,108,226,226,224,1002,223,2,223,
			1005,224,644,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,659,101,1,223,223,1107,226,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]

def opcode_Parameters(opcode, opcodeIndex, opcodeInput):
	# Break dow the instruction into separate pieces
	instructionCode = int(str(opcode[opcodeIndex])[-1])
	try:
		parameter1 = int(str(opcode[opcodeIndex])[-3]) # mode of 1st parameter: 0 = position mode / 1 = immediate mode
	except IndexError:
		parameter1 = 0
	try:
		parameter2 = int(str(opcode[opcodeIndex])[-4]) # mode of 2nd parameter: 0 = position mode / 1 = immediate mode
	except IndexError:
		parameter2 = 0
	try:
		parameter3 = int(str(opcode[opcodeIndex])[-5]) # mode of 3rd parameter (result): 0 = position mode / 1 = immediate mode
	except IndexError:
		parameter3 = 0
	logging.info('Starting opcode: (%s%%), at position: (%s%%)'  % (instructionCode, opcodeIndex))
	# call functions with all parameters and return new index
	if instructionCode == 1:
		opcodeIndex = opcode_One(opcode, opcodeIndex, parameter1, parameter2, parameter3)
	elif instructionCode == 2:
		opcodeIndex = opcode_Two(opcode, opcodeIndex, parameter1, parameter2, parameter3)
	elif instructionCode == 3:
		opcodeIndex = opcode_Three(opcode, opcodeIndex, opcodeInput)
	elif instructionCode == 4:
		opcodeIndex = opcode_Four(opcode, opcodeIndex, parameter1)
	return opcodeIndex

def opcode_One(opcode, i, parameter1, parameter2, parameter3):
	# adds together numbers from two positions and stores the result in a third position: 
	if parameter1 == 0:
		firstNumber = opcode[opcode[i + 1]]
	else:
		firstNumber = opcode[i +1]
	if parameter2 == 0:
		secondNumber = opcode[opcode[i + 2]]
	else:
		secondNumber = opcode[i + 2]
	resultNumber = opcode[i + 3]
	opcode[resultNumber] = firstNumber + secondNumber
	logging.info('result: (%s%%),  in index: (%s%%), FirstNumber: (%s%%), secondNumber: (%s%%), Index: (%s%%)'  % (opcode[resultNumber], resultNumber, firstNumber, secondNumber, i))
	logging.info('Completed opcode 1 at position (%s%%)'  % (i))
	i = i + 4
	return i
	
def opcode_Two(opcode, i, parameter1, parameter2, parameter3):
	# multiplies the two inputs instead, three integers after the opcode indicate where the inputs and outputs are, not their values
	if parameter1 == 0:
		firstNumber = opcode[opcode[i + 1]]
	else:
		firstNumber = opcode[i + 1]
	if parameter2 == 0:
		secondNumber = opcode[opcode[i + 2]]
	else:
		secondNumber = opcode[i + 2]
	resultNumber = opcode[i + 3]
	opcode[resultNumber] = firstNumber * secondNumber 
	logging.info('result: (%s%%),  in index: (%s%%), FirstNumber: (%s%%), secondNumber: (%s%%), Index: (%s%%)'  % (opcode[resultNumber], resultNumber, firstNumber, secondNumber, i))
	logging.info('Completed opcode 2 at position (%s%%)'  % (i))
	i = i + 4
	return i
	
def opcode_Three (opcode, i, opcodeInput):
	# opcode_Three -takes a single integer as input and saves it to the position given by its only parameter.
	resultIndex = opcode[i+1]
	opcode[resultIndex] = opcodeInput
	logging.info('result: (%s%%),  in index: (%s%%)'  % (opcode[resultIndex], resultIndex))	
	logging.info('Completed opcode 3 at position (%s%%)'  % (i))
	i = i +2 
	return i
	
def opcode_Four(opcode, i, parameter1):
	# opcode_Four -outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50
	if parameter1 == 0:
		print('Print OUTPUT: ' + str(opcode[opcode[i+1]]) + ' at index: ' + str(i))
	elif parameter1 == 1:
		print('Print OUTPUT: ' + str(opcode[i+1]) + ' at index: ' + str(i))
	i = i + 2
	return	i


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.info('Start of program')
logging.disable(logging.CRITICAL)

opcodeInput = 1
opcodeIndex = 0 #set starting index for commands

while True:
	if opcode[opcodeIndex] == 99:
		print('Program finished!!!!!')
		break	
	opcodeIndex = opcode_Parameters(opcode, opcodeIndex, opcodeInput)

