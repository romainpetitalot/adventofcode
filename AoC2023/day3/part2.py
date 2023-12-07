res = 0
memo = {}
coords_symbol = []
for row in range(140):
	try:
		l = input()
		# print(l)
		current = ""
		idx = []
		for col, char in enumerate(l+"."):
			# print(idx)
			if char.isdigit():
				current += char
				idx.append((row, col))
			else:
				if len(current)>0:
					val = int(current)
					for coord in idx:
						memo[coord]=(val,idx)
					current = ""
					idx = []
				if char == "*":
					coords_symbol.append((row, col))
				
	except:
		print("iefh")
		break
# print(memo)
for r, c in coords_symbol:
	counted = set()
	nb = 0
	for dr in range(-1, 2):
		for dc in range(-1, 2):
			if (r+dr, c+dc) in memo.keys() and tuple(memo[(r+dr, c+dc)][1] + [(r,c)]) not in counted:
				# res += memo[(r+dr, c+dc)][0]
				# print(memo[(r+dr, c+dc)][0], (r+dr, c+dc))
				# memo[(r+dr, c+dc)][1].append((r,c))
				counted.add(tuple(memo[(r+dr, c+dc)][1] + [(r,c)]))
				nb += 1
	if nb == 2:
		counted = list(counted)
		print(memo[counted[0][0]][0], memo[counted[1][0]][0], memo[counted[0][0]][0] * memo[counted[1][0]][0])
		res += memo[counted[0][0]][0] * memo[counted[1][0]][0]
print(counted)
print(res)

# 522144
# 878144