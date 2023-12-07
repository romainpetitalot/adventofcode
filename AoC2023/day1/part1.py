
r = 0
for i in range(1000):
	s = input()
	first = None
	last = None
	for c in s:
		if c.isdigit():
			last = c
			if first == None:
				first = c
	r += int(first+last)
print(r)