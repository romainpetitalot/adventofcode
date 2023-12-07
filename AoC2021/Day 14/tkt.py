import sys
import numpy as np

transfo = {}
count_couple = {}


for line in sys.stdin:
	s = line.rstrip()
	if '->' in s:
		s = s.split(' -> ')
		transfo[s[0]] = s[1]
		print(s)
	else:
		if len(s)>0:
			chaine = s

for c in transfo.keys():
	count_couple[c] = 0

for i in range(len(chaine)-1):
	count_couple[chaine[i:i+2]] += 1

print(chaine)
print(count_couple)

for t in range(4000):
	add = {}
	for keys, val in count_couple.items():
		if val>0:

			newKeys1 = keys[0] + transfo[keys]
			newKeys2 = transfo[keys] + keys[1]
			print(keys, newKeys1, newKeys2, val)

			if newKeys1 in add.keys():
				add[newKeys1] += val			
			else:
				add[newKeys1] = val

			if newKeys2 in add.keys():
				add[newKeys2] += val			
			else:
				add[newKeys2] = val

			if keys in add.keys():
				add[keys] -= val			
			else:
				add[keys] = -val


	for keys, val in add.items():
		count_couple[keys]+= val

letters = {}

for keys, val in count_couple.items():
	if keys[0] in letters.keys():
		letters[keys[0]] += val
	else:
		letters[keys[0]] = val	

letters[chaine[-1]] += 1

print(max(letters.values()) - min(letters.values()))


# for t in range(15):
# 	print(t)
# 	newChaine = ""
# 	for i in range(len(chaine)-1):
# 		newChaine += chaine[i] + transfo[chaine[i:i+2]] 
# 	chaine = newChaine+chaine[-1]
# 	#if len(chaine)<20:
# 	#	print(chaine)
# 	#print(len(newChaine))

# a, count = np.unique(list(chaine),return_counts = True)
# #print(a, count)
# #print(max(count)-min(count))

# print(count_couple)