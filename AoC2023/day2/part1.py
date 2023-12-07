r = 0
for i in range(100):
	try:
		possible = True
		g = input().split()
		_id = g[1][:-1]
		g = " ".join(g[2:])
		for p in g.split(";"):
			for color in p.split(","):
				nb, c = color.split()
				if c=="blue" and int(nb)>14:
					possible = False
				elif c=="green" and int(nb)>13:
					possible = False
				elif c=="red" and int(nb)>12:
					possible = False
		if possible:
			r += int(_id)
	except:
		break
print(r)