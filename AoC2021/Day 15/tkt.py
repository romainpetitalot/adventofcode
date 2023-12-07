import sys

matrix = []

for line in sys.stdin:
	s = line.rstrip()
	matrix.append( list(map(int, list(s)) ))


m = len(matrix)
n = len(matrix[0])

newMatrix = [[] for i in range(4)]

for t in range(4):
	for l in range(len(matrix)):
		a = list(map(lambda x: x + 1 if x<9 else 1, matrix[l][n*t:n*(t+1)]))
		matrix[l] += a
		newMatrix[t] += [a]

for i in range(4):
	for t in range(4):
		for l in range(len(newMatrix[i])):
			a = list(map(lambda x: x + 1 if x<9 else 1, newMatrix[i][l][n*t:n*(t+1)]))
			newMatrix[i][l] += a

	for l in range(m):
		matrix += [newMatrix[i][l]]



m = len(matrix)
n = len(matrix[0])
dp = [ [-1 for _ in range(n)] for _ in range(m)]
dp[0][0] = 0
for step in range(200): #Au lieu du for on peut faire un while old_dp != dp on continue parce que si dp reste le même après une itération il changera plus
	for y in range(m):
		for x in range(n):
			if(y,x)!=(0,0):
				candidates = [dp[y-1][x] if y > 0 else None, dp[y][x-1] if x > 0 else None, dp[y+1][x] if y < m - 1 else None , dp[y][x+1] if x < n - 1 else None ]
				dp[y][x] = min([c for c in candidates if c!= -1 and  c != None]) + matrix[y][x]

	print(dp[-1][-1])

