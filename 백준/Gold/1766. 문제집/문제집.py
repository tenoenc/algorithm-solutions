import heapq
import sys

input = sys.stdin.readline

queue = []
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
	A, B = map(int, input().split())
	graph[A].append(B)
	indegree[B] += 1

for node in range(1, N+1):
	if indegree[node] == 0:
		heapq.heappush(queue, node)

result = []

while queue:
	cur_node = heapq.heappop(queue)

	result.append(cur_node)

	for adj_node in graph[cur_node]:
		indegree[adj_node] -= 1
		if indegree[adj_node] == 0:
			heapq.heappush(queue, adj_node)

print(*result)