import sys

d0 = "cagedb"

summ = 0

for line in sys.stdin:
	s = line.rstrip().split('|')
	print(s)

	for c in s[0].split():
		if len(c) == 2:
			verif11 = c[0]
			verif12 = c[1]


	for c in s[0].split():
		if len(c) == 6:
			if not(verif11 in c and verif12 in c):
				verif5 = verif11 if verif11 in c else verif12


	for c in s[0].split():
		if len(c) == 4:
			verif91 = c[0]
			verif92 = c[1]
			verif93 = c[2]
			verif94 = c[3]



	r = ""
	for c in s[1].split():
		if len(c) == 2:
			r += "1"
		elif len(c) == 3:
			r += "7"
		elif len(c) == 4:
			r += "4"
		elif len(c) == 7:
			r += "8"

		elif len(c) == 5:
			a = "".join(sorted(list(c)))

			if verif11 in c and verif12 in c:
				r+="3"

			else:
				if verif5 in c:
					r+="5"
				else:
					r+="2" 
			
		elif len(c) == 6:
			# a = "".join(sorted(list(c)))
			if verif11 in c and verif12 in c:
				if verif91 in c and verif92 in c and verif93 in c and verif94 in c:
					r+="9"
				else:
					r+="0"
			else:
				r+="6"


	print(r)
	summ += int(r)
print(summ)

# cefabd cdfgeb
# ab
#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc