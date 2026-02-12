import sys
input = sys.stdin.readline

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
units = [[[] for _ in range(N)] for _ in range(N)]
pos = dict()
dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
for i in range(1, K+1):
	r, c, d = map(int, input().split())
	units[r-1][c-1].append((i, d))
	pos[i] = (r-1, c-1, 0)

turns = 0

while turns <= 1000:
	turns += 1
	# 종료 조건: 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간
	for k in range(1, K+1):
		y, x, z = pos[k]
		_, d = units[y][x][z]
		ny, nx = y + dy[d], x + dx[d]

		# 파란색이거나 범위를 벗어나는 경우
		if not (0 <= ny < N and 0 <= nx < N) or grid[ny][nx] == 2:
			if d == 1:
				nd = 2
			elif d == 2:
				nd = 1
			elif d == 3:
				nd = 4
			else:
				nd = 3
			ny, nx = y + dy[nd], x + dx[nd]
			units[y][x][z] = (k, nd)

			# 반대쪽도 마찬가지인 경우 가만히 있기
			if not (0 <= ny < N and 0 <= nx < N) or grid[ny][nx] == 2:
				continue

		# 흰색인 경우
		if grid[ny][nx] == 0:
			s_idx = len(units[ny][nx])
			temp = units[y][x][z:]
			units[ny][nx].extend(temp)
			units[y][x] = units[y][x][:z]
			for ii, v in enumerate(temp):
				i, d = v
				pos[i] = (ny, nx, s_idx+ii)
		# 빨간색인 경우
		elif grid[ny][nx] == 1:
			s_idx = len(units[ny][nx])
			temp = units[y][x][z:][::-1]
			units[ny][nx].extend(temp)
			units[y][x] = units[y][x][:z]
			for ii, v in enumerate(temp):
				i, d = v
				pos[i] = (ny, nx, s_idx+ii)

		if len(units[ny][nx]) >= 4:
			print(turns)
			exit(0)
else:
	print(-1)