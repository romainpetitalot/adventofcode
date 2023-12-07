import sys

maxX, maxY = 0, 0
dots = []
fold = []

for line in sys.stdin:
	s = line.rstrip()
	if ',' in s:
		s = list(map(int,s.split(',')))
		dots += [(s[1], s[0])]
		maxX = max(maxX, s[0]+1)
		maxY = max(maxY, s[1]+1)

	elif 'fold' in s:
		fold += [s.split()[-1]]


grid = ['.'*(maxX) for j in range(maxY)]

for i in range(maxY):
	for j in range(maxX):
		if (i,j) in dots:
			grid[i] = grid[i][:j] + "#" + grid[i][j+1:]

for i in range(len(fold)):
	axe, val = fold[i].split("=")
	val = int(val)
	newDots = []
	if 'y'==axe:
		for ligne in range(val+1, maxY):
			for colonne in range(maxX):
				if grid[ligne][colonne] == "#":
					ecart = ligne - val
					newDots += [(val-ecart,colonne)]

		for l in range(val, maxY):
			del grid[val]

		maxY = val

		for l in range(maxY):
			for c in range(maxX):
				if (l,c) in newDots:

					grid[l] = grid[l][:c] + "#" + grid[l][c+1:]
	
	else:
		for ligne in range(maxY):
			for colonne in range(val+1, maxX):
				if grid[ligne][colonne] == "#":
					ecart = colonne - val
					newDots += [(ligne,val - ecart)]				

		for l in range(maxY):
			grid[l] = grid[l][:val]

		maxX = val

		for l in range(maxY):
			for c in range(maxX):
				if (l,c) in newDots:

					grid[l] = grid[l][:c] + "#" + grid[l][c+1:]

	

	r = 0
	for l in range(maxY):
		for c in range(maxX):
			if grid[l][c] == "#":
				r += 1
	print(r)
for i in range(len(grid)):
	print(grid[i])