visited = []
queue = []

def bfs(visited, graph, node):
	visited.append(node)
	queue.append(node)

	while queue:
		s = queue.pop(0)
		print(s, end = ' ')

		for neighbor in graph[s]:
			if neighbor not in visited:
				visited.append(neighbor)
				queue.append(neighbor)


if __name__ == '__main__':

	graph = {
	'A' : set(['B', 'C']),
	'B' : set(['A', 'E']),
	'C' : set(['A']),
	'D' : set(['A', 'B', 'E']),
	'E' : set(['B']),
	} 

	bfs(visited, graph, 'C')