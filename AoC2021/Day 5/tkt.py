import sys

start = {}
end = {}

maxX = 0
maxY = 0

count = 0
for line in sys.stdin:
	s = line.rstrip().split()

	st = list(map(int,s[0].split(",")))
	en = list(map(int,s[2].split(",")))

	maxX = max(maxX, st[0], en[0])
	maxY = max(maxY, st[1], en[1])

	
	start[count] = []
	end[count] = []
	start[count] += st 
	end[count] += en

	count += 1

grid = [[0 for i in range(maxX+1)]for y in range(maxY+1)]


points = []
for i in range(count):
	
	st = start[i]
	en = end[i]
	if st[0]==en[0] or st[1]==en[1]:
		for y in range(min(st[1],en[1]), max(st[1],en[1])+1):
			for x in range(min(st[0],en[0]), max(st[0],en[0])+1):
				points += [(x,y)]
	else:
		dirX = 1 if st[0]<en[0] else -1
		dirY = 1 if st[1]<en[1] else -1

		for c in range(abs(en[0]-st[0])+1):
			points += [(st[0]+c*dirX, st[1]+c*dirY)]


print(points)

for i in range(len(points)):
	pt = points[i]
	grid[pt[1]][pt[0]] += 1

print(grid)

r =0

for i in range(maxY+1):
	for y in range(maxX+1):
		if grid[i][y]>1:
			r += 1
print(r)