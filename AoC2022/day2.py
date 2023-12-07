r = 0
while True:
	try:
		a, b = input().split()

		if b == "X":
			if a == "A":
				r += 3
			elif a=="B":
				r += 1
			else:
				r += 2
		elif b == "Y":
			r += 3
			r += ord(a)-ord("A")+1
		else:
			r += 6
			if a == "A":
				r += 2
			elif a=="B":
				r += 3
			else:
				r += 1

	except:
		print(r)
		break