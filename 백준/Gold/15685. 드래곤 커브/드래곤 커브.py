N = int(input())
grid = [[False] * 101 for _ in range(101)]
dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]


def make_curve(sx, sy, d, g):
	def recursive(depth, cy, cx, path):
		if depth == g:
			return

		new_path = []
		new_path.extend(path)

		for d in path[::-1]:
			d = (d + 1) % 4
			cy, cx = cy + dy[d], cx + dx[d]
			new_path.append(d)
			if 0 <= cy < 101 and 0 <= cx < 101:
				grid[cy][cx] = True

		recursive(depth+1, cy, cx, new_path)

	grid[sy][sx] = True
	ny, nx = sy + dy[d], sx + dx[d]
	if 0 <= ny < 101 and 0 <= nx < 101:
		grid[ny][nx] = True
	recursive(0, ny, nx, [d])

for i in range(N):
	x, y, d, g = map(int, input().split())
	make_curve(x, y, d, g)

answer = 0

for i in range(100):
	for j in range(100):
		if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]:
			answer += 1

print(answer)
