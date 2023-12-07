import sys
import numpy as np

for line in sys.stdin:
	s = list(map(int,line.rstrip().split(',')))

u, count = np.unique(s, return_counts = True)

print(u, count)

u = list(u)
count = list(count)

for jour in range(256):
	toDel = []
	nbDel = 0
	for i in range(len(u)):
		if u[i]>0:
			if u[i]-1 in u[:i]:
				ind = u.index(u[i]-1)
				count[ind] += count[i]
				toDel += [i-nbDel]
				nbDel += 1
				u[i] -= 1
			else:
				u[i] -= 1
		else:
			u[i] = 6
			u.append(8)

			count += [count[i]]
	

	for i in range(len(toDel)):
		del u[toDel[i]]
		del count[toDel[i]]

	print(u)
	print(count)

	print(jour)

print(u, count)
print(sum(count))