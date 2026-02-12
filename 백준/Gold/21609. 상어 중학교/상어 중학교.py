from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

# 가장 큰 블록 그룹 찾기
def find_largest_block_group():
	visited = [[False] * N for _ in range(N)]

	def get_block_group(sy, sx):
		rep_block = grid[sy][sx]		
		queue = deque([(sy, sx)])
		visited[sy][sx] = True
		blocks = [(sy, sx)]
		rainbow_blocks = []

		while queue:
			cy, cx = queue.popleft()

			for i in range(4):
				ny, nx = cy + dy[i], cx + dx[i]
				if not (0 <= ny < N and 0 <= nx < N):
					continue
				if not (grid[ny][nx] == rep_block or grid[ny][nx] == 0):
					continue
				if visited[ny][nx]:
					continue
				if grid[ny][nx] == 0:
					rainbow_blocks.append((ny, nx))

				visited[ny][nx] = True
				blocks.append((ny, nx))
				queue.append((ny, nx))

		for ry, rx in rainbow_blocks:
			visited[ry][rx] = False

		if len(blocks) >= 2:
			return (len(rainbow_blocks), sy, sx, blocks)
		else:
			return None

	max_cnt = -1
	block_info = []
	for i in range(N):
		for j in range(N):
			if grid[i][j] > 0 and not visited[i][j]:
				result = get_block_group(i, j)
				if not result:
					continue
				len_block_group = len(result[3])
				if len_block_group > max_cnt:
					block_info = [result]
					max_cnt = len_block_group
				elif len_block_group == max_cnt:
					block_info.append(result)

	if block_info:
		block_info.sort(key=lambda x: (-x[0], -x[1], -x[2]))
		return block_info[0][3]
	else:
		return []

def gravity():
	for j in range(N):
		for i in range(N-2, -1, -1):
			if grid[i][j] >= 0:
				k = i
				while k+1 < N and grid[k+1][j] == -2:
					grid[k+1][j], grid[k][j] = grid[k][j], grid[k+1][j]
					k += 1

ans = 0

while True:
	# 크기가 가장 큰 블록 그룹을 찾음
	largest_block_group = find_largest_block_group()

	# 블록 그룹이 존재하지 않으면 반복 종료
	if not largest_block_group:
		break

	ans += len(largest_block_group) ** 2

	# 찾은 블록 그룹의 모든 블록 제거
	for y, x in largest_block_group:
		grid[y][x] = -2

	# 격자에 중력이 작용
	gravity()

	# 격자가 90도 반시계 방향으로 회전
	grid = [list(col) for col in zip(*map(reversed, grid))]

	# 격자에 중력이 작용
	gravity()

print(ans)