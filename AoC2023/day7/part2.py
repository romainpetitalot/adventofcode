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

order = "A,K,Q,T,9,8,7,6,5,4,3,2,J"[::-1].split(",")

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
	# hand = sorted(hand, key=lambda x:order.index(x))
	maxi = -1
	for j in "A,K,Q,T,9,8,7,6,5,4,3,2":
		newHand = hand.replace("J",j)
		c = Counter(newHand)
		if any([v==5 for v in c.values()]):
			tmp = val[5]
		elif any([v==4 for v in c.values()]):
			tmp = val[4]
		elif any([v==3 for v in c.values()]) and any([v==2 for v in c.values()]):
			tmp = val[32]
		elif any([v==3 for v in c.values()]):
			tmp = val[3]
		elif any([v==2 for v in c.values()]) and len(c.values())==3:
			tmp = val[22]
		elif any([v==2 for v in c.values()]):
			tmp = val[2]
		else:
			tmp = val[1]
		maxi = max(maxi, tmp)
	res += maxi
	for h, i in zip(hand, [100000000, 1000000, 10000, 100, 1]):
		res += (order.index(h)+1)*i
	return res

l.sort(key=lambda x:compute_score(x[0]))

print(*l, sep="\n")

print(sum((i+1)*a[1] for i,a in enumerate(l)))

# 253630098