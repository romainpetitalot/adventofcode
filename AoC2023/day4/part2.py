res = [1 for i in range(2000)]
for t in range(2000):
	try:
		l = " ".join(input().split(":")[1:])
		*win, = map(int, l.split("|")[0].split())
		*a, = map(int, l.split("|")[1].split())
		# print([aa in win for aa in a])
		# res += 2**sum(aa in win for aa in a)//2
		for i in range(sum(aa in win for aa in a)):
			res[t+i+1] += res[t]	
	except:
		break
print(t)
print(sum(res[:t]))
print(res[:t])