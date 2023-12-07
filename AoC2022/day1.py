tmp = 0
maxi = 0
l = []
while True:
	try:
		a = input()
		if len(a)>0:
			tmp += int(a)
		else:
			l.append(tmp)
			tmp = 0
	except:
		l.append(tmp)
		l.sort(reverse=True)
		print(*(l[:3]))
		print(sum(l[:3]))
		break