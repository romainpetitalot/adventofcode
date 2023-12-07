import sys

summ = 0

tuple_add = lambda a, b: tuple(i+j for i, j in zip(a, b))

def parcoursEnLargeur(coord, tailleX, tailleY):
	q = []
	visited = [coord] 
	q += [coord]

	nb = 1

	adjacent = [(-1, 0),(0, -1),(0, 1),(1, 0)]

	while len(q)>0:
		# print(q)
		currentC = q.pop(0)
		
		for i in range(4):
			voisin = tuple_add(currentC, adjacent[i])
			
			if 0<=voisin[0]<tailleY and 0<=voisin[1]<tailleX:
				if grid[voisin[0]][voisin[1]] < 9 and voisin not in visited:
					print(voisin, visited)
					nb += 1
					q += [voisin]
					visited += [voisin]
	return nb


grid = []
for line in sys.stdin:
	s = line.rstrip()
	grid += [list(map(int, list(s)))]

lowP = []

for i in range(len(grid)):
	for j in range(len(grid[0])):
		val = grid[i][j]

		check = [(i-1,j), (i, j-1), (i+1,j), (i, j+1)]
		bon = True
		for d in check:
			if 0<=d[0]<len(grid) and 0<=d[-1]<len(grid[i]):
				if grid[d[0]][d[-1]]<=val:
					bon = False

		if bon:
			lowP += [(i,j)]


tailles = []
for coord in lowP:

	tailles += [parcoursEnLargeur(coord, len(grid[0]), len(grid))]

tailles.sort()

print(tailles[-3]*tailles[-2]*tailles[-1])
