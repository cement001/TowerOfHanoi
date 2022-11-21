# cement001
# Challenge assignment for Data Structures class
# Start date: 11/08/2022
# Finish date: ll/18/2022

# Tower of Hanoi (List Output version)
#
# Objective: to move the tower from the first peg to the last peg.
# - Must move only one ring at a time.
# - Cannot move a larger ring on top of a smaller ring.


# RESTRICTIONS:
# can't use reverse(), delete(), remove(), pop(), insert()


# Basic logical findings:
# pole1 --> if number of rings is odd, move top ring to slot three, if even, move top ring to slot two.
# pole2 --> if number of rings is odd, move top ring to slot three, if even, move top ring to slot one.
# pole3 --> if number of rings is odd, move top ring to slot two, if even, move top ring to slot one.



############################################################################## INPUT/OUTPUT ################################################################################

# Ask for number of rings, repeat process until user enters within range.

rings = int(input("Enter number of rings between 3 and 9.\n--> "))
while rings > 9 or rings < 3:
	print("Error: Input outside expected range.")
	rings = int(input("Enter number of rings between 3 and 9.\n--> "))

# Assign descending list to <goal> and <pole1>; will be useful for later judgment.  <pole2> and
# <pole3> are empty lists representing the two other currently empty poles.

pole1 = [rings-s for s in range(rings)]
goal = [rings-s for s in range(rings)]

pole2 = []
pole3 = []

# Print each list, where each number corresponds to the ring's value

def printPoles():
	print(f"\n{pole1}\n{pole2}\n{pole3}\n")

printPoles()

############################################################################# ALGORITHMIC FUNCTIONS ########################################################################

# Function that performs the action pop() usually performs, but instead returns the new list.
# Necessary to work around the restriction of not using pop().

def newPop(pole):
	if len(pole) == 1:
		return []
	smallerPole = [pole[f] for f in range(len(pole)-1)]
	return smallerPole

# Function that determines whether the top ring of the destination pole is larger than the moving
# ring by an even amount (making them both odd or both even).  This case comes up repeatedly, and 
# this function mainly exists to prevent the program from undoing actions, which most often results 
# in an infinite loop.

def notSameParity(fromVal, toVal):
	nNO = True
	for w in range(2, 10, 2):
		if fromVal + w == toVal:
			nNO = False
	return nNO

# CENTRAL LOGICAL COMPONENT
#
# Function that determines how to move the top ring from the first pole to another pole:
#
# If the total number of rings on the first pole is even, the top ring needs to be moved to the
# second pole.  This can only happen if the second pole is empty or if the top ring of the second
# pole is larger than the top ring of the first pole.
#
# If the total number of rings on the first pole is odd, the top ring needs to be moved to the
# third pole.  This can only happen if the third pole is empty or if the top ring of the third
# pole is larger than the top ring of the first pole by an odd amount.

def push1():
	global pole1
	global pole2
	global pole3
	if len(pole1) % 2 == 0:
		if len(pole2) == 0 or pole2[-1] > pole1[-1]:
			pole2.append(pole1[-1])
			pole1 = newPop(pole1)
			printPoles()
			return True
		return False
	else:
		if len(pole3) == 0 or (pole3[-1] > pole1[-1] and notSameParity(pole1[-1], pole3[-1])):
			pole3.append(pole1[-1])
			pole1 = newPop(pole1)
			printPoles()
			return True
		return False

# CENTRAL LOGICAL COMPONENT
#
# Function that determines how to move the top ring from the second pole to another pole:
#
# If the total number of rings on the second pole is even, the top ring needs to be moved to the
# first pole.  This can only happen if the first pole is empty or if the top ring of the first
# pole is larger than the top ring of the second pole by an odd amount.
#
# If the total number of rings on the second pole is odd, the top ring needs to be moved to the
# third pole.  This can only happen if the top ring of the third pole is larger than the top ring
# of the second pole.


def push2():
	global pole1
	global pole2
	global pole3
	if len(pole2) % 2 == 0:
		if len(pole1) == 0 or (pole1[-1] > pole2[-1] and notSameParity(pole2[-1], pole1[-1])):
			pole1.append(pole2[-1])
			pole2 = newPop(pole2)
			printPoles()
			return True
		return False
	else:
		if pole3[-1] > pole2[-1]:
			pole3.append(pole2[-1])
			pole2 = newPop(pole2)
			printPoles()
			return True
		return False

# Function that determines whether adding a ring to a pole would cause that pole to be sequential.
# This is only important for moving rings from the third pole to the first pole, as if this is not
# implemented, the program will undo many of its actions and cause an infinite loop.

def isNotSequential(p, newV):
	temp = []
	for n in p:
		temp.append(n)
	temp.append(newV)
	seq = False
	for g in range(len(temp)-1):
		if temp[g] != temp[g+1]:
			seq = True
	return seq

# CENTRAL LOGICAL COMPONENT
#
# Function that determines how to move the top ring from the third pole to another pole:
#
# If the total number of rings on the third pole is even, the top ring needs to be moved to the
# first pole.  This can only happen if the first pole has at least one ring on it that is larger
# than the top ring of the third pole, and if the bottom ring of the first pole is the largest in
# the program, the addition of the top ring of the third pole does not leave the first pole in
# a perfectly sequential order.
#
# If the total number of rings on the third pole is odd, the top ring needs to be moved to the
# second pole.  This can only happen if the top ring of the second pole is larger than the top ring
# of the third pole by an odd amount.

def push3():
	global pole1
	global pole2
	global pole3
	if len(pole3) % 2 == 0:
		if len(pole1) > 0 and pole1[-1] > pole3[-1] and ((pole1[0] == rings and isNotSequential(pole1, pole3[-1])) or (pole1[0] != rings)):
			pole1.append(pole3[-1])
			pole3 = newPop(pole3)
			printPoles()
			return True
		return False
	else:
		if len(pole2) > 0 and (pole2[-1] > pole3[-1] and notSameParity(pole3[-1], pole2[-1])):
			pole2.append(pole3[-1])
			pole3 = newPop(pole3)
			printPoles()
			return True
		return False


################################################################################### APPLICATION ############################################################################

# MAIN LOOP
#
# The order of movement judgment starts with the first pole, then goes to the second pole, and then
# goes to the third pole.  Each judgment can only be made if the pole has at least one ring on it,
# and in the case of the second pole, can only be made if the third pole has at least one ring on it.
#
# After each cycle of judgment, the program evaluates whether the third pole looks the same as the
# goal pole, and if it does, terminates the program with a completion message.

while True:
	pole1Mov = True
	pole2Mov = True
	pole3Mov = True
	complete = True

	while pole1Mov and len(pole1) > 0:
		pole1Mov = push1()

	while pole3Mov and len(pole3) > 0:
		pole3Mov = push3()

	while pole2Mov and len(pole3) > 0 and len(pole2) > 0:
		pole2Mov = push2()

	if len(pole3) == len(goal):
		for i in range(len(pole3)):
			if pole3[i] != goal[i]:
				complete = False
	else:
		complete = False

	if complete:
		print("Tower Complete")
		break
