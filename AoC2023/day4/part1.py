res = 0
for t in range(2000):
	try:
		current = 0
		l = " ".join(input().split(":")[1:])
		*win, = map(int, l.split("|")[0].split())
		*a, = map(int, l.split("|")[1].split())
		# print([aa in win for aa in a])
		res += 2**sum(aa in win for aa in a)//2
	except:
		break
print(res)