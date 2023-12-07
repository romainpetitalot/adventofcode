import sys
from collections import deque

found = []

def find_paths_dfs(graph, start, end):
	stack = deque()
	stack.append((start, [start]))
	count = 0

	global found

	while stack:

		(node, path) = stack.pop()
		adjacent_nodes = [n for n in graph[node] if n not in path or n.isupper()]
		for adjacent_node in adjacent_nodes:
			if adjacent_node == end:
				print(path + [adjacent_node])
				count += 1
				found += [path + [adjacent_node]]
			else:
				stack.append((adjacent_node, path + [adjacent_node]))

	return count

def find_paths_dfs_bonus(graph, start, end, bonus):
	stack = deque()
	stack.append((start, [start]))
	count = 0
	used = False

	global found

	while stack:

		(node, path) = stack.pop()
		adjacent_nodes = [n for n in graph[node] if n not in path or n.isupper() or (n==bonus and path.count(n)==1)]
		# if bonus in graph[node] and bonus in path and bonus not in adjacent_nodes and not used:
		# 	adjacent_nodes += [bonus]
		# 	used = True
		for adjacent_node in adjacent_nodes:
			if adjacent_node == end:
				if path + [adjacent_node] not in found:
					# print(path + [adjacent_node])
					count += 1
					found += [path + [adjacent_node]]
			else:
				stack.append((adjacent_node, path + [adjacent_node]))

	return count


graph = {}
for line in sys.stdin:
	s = line.rstrip().split('-')
	if s[0] not in graph.keys():
		graph[s[0]] = []
	if s[1] not in graph.keys():
		graph[s[1]] = []
	graph[s[0]] += [s[1]]
	graph[s[1]] += [s[0]]

bonus = []
for c in graph.keys():
	if c.islower() and c not in ['start', 'end']:
		bonus += [c]

found = []

r = find_paths_dfs(graph, 'start', 'end')
print(r, bonus)


print(len(bonus))
for i in range(len(bonus)):
	r += find_paths_dfs_bonus(graph, 'start', 'end', bonus[i])
	print(i,r)

# found.sort()

# for i in found:
# 	print(i)
