from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	sy, sx = map(int, input().split())
	pos = [list(map(int, input().split())) for _ in range(n)]
	ry, rx = map(int, input().split())

	visited = [False] * n

	queue = deque([(sy, sx)])

	while queue:
		cy, cx = queue.popleft()

		if abs(cy-ry) + abs(cx-rx) <= 20 * 50:
			print("happy")
			break

		for i, v in enumerate(pos):
			ny, nx = v
			diff = abs(cy-ny) + abs(cx-nx)
			nbeers = 20 - diff // 50
			if nbeers >= 0 and not visited[i]:
				visited[i] = True
				queue.append((ny, nx))
	else:
		print("sad")