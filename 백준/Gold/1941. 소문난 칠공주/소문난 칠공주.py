from collections import deque
from itertools import combinations

N = 5
grid = [input() for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

ans = 0

for comb in combinations([(i, j) for j in range(5) for i in range(5)], 7):
	def bfs(sy, sx):
		queue = deque([(sy, sx)])
		visited = [[False] * 5 for _ in range(5)]
		visited[sy][sx] = True
		scnt = 1 if grid[sy][sx] == 'S' else 0
		ycnt = 1 - scnt

		while queue:
			y, x = queue.popleft()

			for i in range(4):
				ny, nx = y + dy[i], x + dx[i]
				if (ny, nx) in comb and not visited[ny][nx]:
					visited[ny][nx] = True
					queue.append((ny, nx))
					if grid[ny][nx] == 'S':
						scnt += 1
					else:
						ycnt += 1

		return scnt + ycnt == 7 and scnt >= 4

	if bfs(*comb[0]):
		ans += 1

print(ans)