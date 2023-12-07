from collections import Counter
hands = []
bids = []
l = []
for i in range(1000):
	try:
		hand, bid = input().split()
		l.append((hand, int(bid)))
		# bids.append(int(bid))

	except EOFError:
		break

order = "A,K,Q,J,T,9,8,7,6,5,4,3,2"[::-1].split(",")

val={}
val[5]=99999999999999999999999999999**2
val[4]=99999999999999999999999999**2
val[32]=999999999999999999999999**2
val[3]=9999999999999999999999**2
val[22]=99999999999999999999**2
val[2]=999999999999999999**2
val[1]=9999999999999999**2

def compute_score(hand):
	res = 0
	c = Counter(hand)
	# hand = sorted(hand, key=lambda x:order.index(x))
	if any([v==5 for v in c.values()]):
		res += val[5]
	elif any([v==4 for v in c.values()]):
		res += val[4]
	elif any([v==3 for v in c.values()]) and any([v==2 for v in c.values()]):
		res += val[32]
	elif any([v==3 for v in c.values()]):
		res += val[3]
	elif any([v==2 for v in c.values()]) and len(c.values())==3:
		res += val[22]
	elif any([v==2 for v in c.values()]):
		res += val[2]
	else:
		res += val[1]

	for h, i in zip(hand, [100000000, 1000000, 10000, 100, 1]):
		res += (order.index(h)+1)*i
	return res

l.sort(key=lambda x:compute_score(x[0]))

print(*l, sep="\n")

print(sum((i+1)*a[1] for i,a in enumerate(l)))

# 252008590