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
	'A' : set(['0', '1']),
	'B' : set(['0', '2']),
	'C' : set(['2', '3', '4']),
	'D' : set(['A', 'B', '2']),
	'E' : set(['3', '4', 'B']),
	} 

	bfs(visited, graph, 'C')