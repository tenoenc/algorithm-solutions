from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

def can_open(door):
	return mkeys & (1 << (door.lower() - ord('A')))

T = int(input())
for _ in range(T):
	h, w = map(int, input().split())
	grid = ['.' + input() + '.' for _ in range(h)]
	grid.insert(0, '.' * (w+2))
	grid.append('.' * (w+2))

	h += 2
	w += 2

	visited = [[False] * w for _ in range(h)]

	temp_keys = input()
	keys = [False] * 26
	if temp_keys != "0":
		for k in temp_keys:
			keys[ord(k) - ord('a')] = True

	locked_doors = [[] for _ in range(26)]

	doc_count = 0
	queue = deque([(0, 0)])
	visited[0][0] = True

	while queue:
		y, x = queue.popleft()

		for i in range(4):
			ny, nx = y + dy[i], x + dx[i]

			if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] != '*' and not visited[ny][nx]:
				cell = grid[ny][nx]

				if cell == '.':
					visited[ny][nx] = True
					queue.append((ny, nx))

				elif cell == '$':
					doc_count += 1
					visited[ny][nx] = True
					queue.append((ny, nx))

				elif 'A' <= cell <= 'Z':
					door_idx = ord(cell) - ord('A')
					if keys[door_idx]:
						visited[ny][nx] = True
						queue.append((ny, nx))
					else:
						visited[ny][nx] = True
						locked_doors[door_idx].append((ny, nx))
				elif 'a' <= cell <= 'z':
					visited[ny][nx] = True
					queue.append((ny, nx))

					key_idx = ord(cell) - ord('a')
					if not keys[key_idx]:
						keys[key_idx] = True
						while locked_doors[key_idx]:
							dy_door, dx_door = locked_doors[key_idx].pop()
							queue.append((dy_door, dx_door))

	print(doc_count)
	