
r = 0
for i in range(1000):
	s = input()
	nb = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	for n,m in zip(nb, range(1,10)):
		s = s.replace(n,  n+str(m)+n)
	first = None
	last = None
	for c in s:
		if c.isdigit():
			last = c
			if first == None:
				first = c
	print(int(first+last))
	r += int(first+last)
print(r)