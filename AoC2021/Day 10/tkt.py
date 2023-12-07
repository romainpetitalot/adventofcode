import sys


ferme = ["()", "[]", "{}", "<>"]

val = [3, 1, 2, 4]

d = "{([<"
f = "})]>"

rS = []

for line in sys.stdin:
	s = line.rstrip()
	r=0
	counter = 0
	Trouve = False
	while not(Trouve):
		if counter > 10000:
			s = s[::-1]
			newS = ""
			for i in range(len(s)):
				newS += f[d.index(s[i])]
			 	
			for i in range(len(s)):
				r *= 5
				r += val[f.index(newS[i])]
			rS += [r]
			print(newS)
			Trouve = True
		for i in range(len(s)-1):
			if s[i] in d:
				incD = d.index(s[i])
				if s[i+1] in f:
					incF = f.index(s[i+1])
					if incD == incF:
						s = s[:i]+s[i+2:]
						break
					else:
						r += val[incF]
						#print(s)
						#print(i,f[incF], val[incF])
						Trouve = True
						break

		counter += 1
rS.sort()
print(rS[len(rS)//2])
