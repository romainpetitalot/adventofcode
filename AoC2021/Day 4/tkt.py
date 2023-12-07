import sys
import copy


MAX = 100

count = -1
boards = {}
boardState = {}
for i in range(MAX):
	boards[i] = []
	boardState[i] = [[False for h in range(5)] for j in range(5)]
number = []

for line in sys.stdin:
	s = line.rstrip()
	if "," in s:
		number += list(map(int,s.split(',')))

	elif s == "":
		count += 1
	else:
		boards[count] += [list(map(int,s.split()))]	



def add(val):
	for i in range(MAX):
		for j in range(5):
			for h in range(5):
				if boards[i][j][h] == val:
					boardState[i][j][h] = True

def checkline():
	for i in range(MAX):
		if i not in winningBoards:
			for j in range(5):
				if boardState[i][j] == [True for h in range(5)]:
					return i
	return -1

def checkcolumn():
	for i in range(MAX):
		if i not in winningBoards:
			for j in range(5):
				ful = True
				for h in range(5):
					if not boardState[i][h][j]:
						ful = False
				if ful:
					return i
	return -1
def full():
	wins = []
	for i in range(MAX):
		if i not in winningBoards:
			for j in range(5):
				if boardState[i][j] == [True for h in range(5)]:
					wins += [i]

			if i not in wins:
				for j in range(5):
					ful = True
					for h in range(5):
						if not boardState[i][h][j]:
							ful = False
					if ful:
						wins += [i]
	
	return wins

winningBoards = []
for i in range(len(number)):
	val = number[i]
	add(val)
	nb = full()
	if len(nb)>=0:
		winningBoards += nb		
	if len(winningBoards) == MAX:
		break

summ = 0

nb = winningBoards[-1]

for j in range(5):
	for h in range(5):
		if not boardState[nb][j][h]:
			summ+= boards[nb][j][h]

print(summ * val, winningBoards)

