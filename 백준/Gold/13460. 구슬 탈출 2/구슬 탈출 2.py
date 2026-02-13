from collections import deque

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(N):
	for j in range(M):
		if grid[i][j] == "R":
			ry, rx = i, j
			grid[i][j] = "."
		elif grid[i][j] == "B":
			by, bx = i, j
			grid[i][j] = "."
		elif grid[i][j] == "O":
			hy, hx = i, j
			grid[i][j] = "."

queue = deque([((ry, rx, "R"), (by, bx, "B"), 0)])
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[ry][rx][by][bx] = True

while queue:
	red, blue, cnt = queue.popleft()

	if (red[0], red[1]) == (hy, hx):
		print(cnt)
		exit(0)

	if cnt == 10:
		continue

	for d in range(4):
		nry, nrx, nby, nbx = red[0], red[1], blue[0], blue[1]
		candidates = [red, blue]

		if d == 0:
			candidates.sort(key=lambda x: -x[1])
		elif d == 1:
			candidates.sort(key=lambda x: -x[0])
		elif d == 2:
			candidates.sort(key=lambda x: x[1])
		else:
			candidates.sort(key=lambda x: x[0])

		for y, x, color in candidates:
			cy, cx = y, x
			ny, nx = cy+dy[d], cx+dx[d]

			while grid[ny][nx] == ".":
				if (color == "R" and (ny, nx) == (nby, nbx)) or (color == "B" and (ny, nx) == (nry, nrx) and (nry, nrx) != (hy, hx)):
					break

				cy, cx = ny, nx
				ny, nx = cy+dy[d], cx+dx[d]

				if (cy, cx) == (hy, hx):
					break

			if color == "R":
				nry, nrx = cy, cx
			else:
				nby, nbx = cy, cx

		if visited[nry][nrx][nby][nbx]:
			continue
		if (nby, nbx) == (hy, hx):
			continue
		visited[nry][nrx][nby][nbx] = True
		queue.append(((nry, nrx, "R"), (nby, nbx, "B"), cnt+1))

print(-1)