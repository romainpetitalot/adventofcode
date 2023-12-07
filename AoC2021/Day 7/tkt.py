import sys

for line in sys.stdin:
	s = list(map(int,line.rstrip().split(',')))

r = []
for i in range(max(s)):
	summ = 0
	for j in range(len(s)):
		a = sum([i for i in range(abs(s[j]-i)+1)])
		summ += a 
	r += [summ]
	print(i)
print(min(r))