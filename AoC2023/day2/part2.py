r = 0
for i in range(100):
	try:
		possible = True
		g = input().split()
		_id = g[1][:-1]
		g = " ".join(g[2:])
		mini = {}
		mini["blue"]=-1
		mini["red"]=-1
		mini["green"]=-1
		for p in g.split(";"):
			for color in p.split(","):
				nb, c = color.split()
				mini[c] = max(mini[c], int(nb))
		r += mini["blue"]*mini["red"]*mini["green"]
	except:
		break
print(r)