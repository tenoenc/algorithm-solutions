import heapq
import sys

input = sys.stdin.readline

n = int(input())

lines = []

for _ in range(n):
	h, o = map(int, input().split())
	s, e = min(h, o), max(h, o)
	lines.append((s, e))

lines.sort(key=lambda x: x[1])

d = int(input())
queue = []
ans = 0

for s, e in lines:
	if e - s > d:
		continue

	heapq.heappush(queue, s)

	while queue and e - d > queue[0]:
		heapq.heappop(queue)

	ans = max(ans, len(queue))

print(ans)