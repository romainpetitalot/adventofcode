*seeds, = map(int, input().split()[1:])
seeds_range = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]

maps = [[] for i in range(7)]
idx_map = -1
for i in range(1000):
	try:
		l = input()
		if "map" in l or ""==l:
			idx_map += 1
		else:
			dest, source, _range = map(int, l.split())
			maps[idx_map//2].append((dest, source, _range))
	except EOFError:
		break

for i in range(7):
    maps_val = maps[i]
    _next = []
    while seeds_range:
        start, end = seeds_range.pop()
        print(start, end, maps_val)
        for dest, source, length in maps_val:
            print(dest, source, length)
            overlap_start = max(start, source)
            overlap_end = min(end, source + length)
            print(overlap_start, overlap_end)
            if overlap_start < overlap_end:
                _next.append((overlap_start - source + dest, overlap_end - source + dest))
                if overlap_start > start:
                    seeds_range.append((start, overlap_start))
                if end > overlap_end:
                    seeds_range.append((overlap_end, end))
                break
        else:
            _next.append((start, end))

    seeds_range = _next
    print()

print(min(seeds_range)[0])

