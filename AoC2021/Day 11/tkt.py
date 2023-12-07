import sys

grid = []
for line in sys.stdin:
	s = list(map(int,list(line.rstrip())))
	grid += [s]

count = 0

for t in range(2000):
	oldCount = count
	explosed = []
	for i in range(10):
		for j in range(10):
			grid[i][j] += 1
	boom = True
	while boom:
		boom = False
		for i in range(10):
			for j in range(10):
				if grid[i][j]>9:
					count += 1
					grid[i][j] = 0
					explosed += [(i,j)]
					boom = True

					for y in range(3):
						for x in range(3):
							if (i+y-1,j+x-1) not in explosed:
								if 0<=i+y-1<10 and 0<=j+x-1<10:
									grid[i+y-1][j+x-1] += 1




	for i in range(10):
		print(*grid[i])
	print()

	if count - oldCount == 100:
		print("tours", t+1)
		break

print(count)