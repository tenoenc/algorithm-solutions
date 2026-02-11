import heapq
import sys

input = sys.stdin.readline

INF = float('inf')

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	u, v, w = map(int, input().split())
	graph[u].append([v, w])

s, e = map(int, input().split())

def dijkstra(start_node):
	queue = [[0, start_node]]
	dist = [INF] * (n+1)
	dist[start_node] = 0
	path = [[] for _ in range(n+1)]
	path[start_node].append(start_node)

	while queue:
		cur_dist, cur_node = heapq.heappop(queue)

		if cur_dist > dist[cur_node]:
			continue

		for adj_node, adj_dist in graph[cur_node]:
			cost = dist[cur_node] + adj_dist
			if cost < dist[adj_node]:
				dist[adj_node] = cost
				heapq.heappush(queue, [cost, adj_node])
				path[adj_node] = path[cur_node] + [adj_node]

	return dist, path

dist, path = dijkstra(s)

print(dist[e])
print(len(path[e]))
print(*path[e])