graph = {
'0': set(['1', '2']),
'1': set(['0', '3', '4']),
'2': set(['0']),
'3': set(['1']),
'4': set(['2', '3'])
}

def dfs(graph, start, visited = []):
	visited.append(start)

	for v in graph[start]:
		if v not in visited:
			visited = dfs(graph, v, visited)
	return visited

print(dfs(graph, '3'))