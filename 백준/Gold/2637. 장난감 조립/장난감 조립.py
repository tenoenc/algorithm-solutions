import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
queue = deque()
cnt = dict()

for _ in range(M):
	v, u, w = map(int, input().split())
	graph[u].append((v, w))
	indegree[v] += 1

for i in range(1, N+1):
	if indegree[i] == 0:
		cnt[i] = dict()
		cnt[i][i] = 1
		queue.append(i)

while queue:
	node = queue.popleft()

	if node == N:
		continue

	for adj_node, adj_cnt in graph[node]:
		for pnode in cnt[node]:
			if adj_node not in cnt:
				cnt[adj_node] = defaultdict(int)
			cnt[adj_node][pnode] += cnt[node][pnode] * adj_cnt

		indegree[adj_node] -= 1
		if indegree[adj_node] == 0:
			queue.append(adj_node)

for i in sorted(cnt[N]):
	print(i, cnt[N][i])
