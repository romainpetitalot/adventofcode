r = 0
count = 0
s = []
while True:
	try:
		if count>2:
			count = 0
			for l in s[0]:
				if l in s[1] and l in s[2]:
					r += 26 if l.isupper() else 0
					r += ord(l.lower()) - ord('a') + 1
					break
			s = []
		else:
			a = input()
			s.append(set(a))
			count += 1

	except:
		print(r)
		break