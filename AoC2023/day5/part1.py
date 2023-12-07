*seeds, = map(int, input().split()[1:])

maps = [{} for i in range(7)]
idx_map = -1
for i in range(1000):
	try:
		l = input()
		if "map" in l or ""==l:
			idx_map += 1
		else:
			dest, source, _range = map(int, l.split())
			maps[idx_map//2][(source, source+_range-1)] = dest-source
	except EOFError:
		break

# print(maps)
res = 99**99
for seed in seeds:
	for i in range(7):
		for mini, maxi in maps[i].keys():
			if mini<=seed<=maxi:
				seed += maps[i][(mini, maxi)] 
				break

	res = min(res, seed)
print(res)

