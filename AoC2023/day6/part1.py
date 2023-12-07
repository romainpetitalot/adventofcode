*time, = map(int, input().split()[1:])
*distance, = map(int, input().split()[1:])
print(time)
res = 1
for t, d in zip(time, distance):
	print(t,d)
	current = 0
	for tt in range(1, t):
		if (t-tt)*tt > d:
			current += 1
	print(current)
	res *= current
print(res)
# 37510 too low