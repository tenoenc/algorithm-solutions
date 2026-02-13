import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
sharks = dict()
cx = -1
dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]

for _ in range(M):
	r, c, s, d, z = map(int, input().split())
	sharks[(r-1, c-1)] = (s, d-1, z)

ans = 0

for _ in range(C):
	cx += 1
	for cy in range(R):
		if (cy, cx) in sharks:
			ans += sharks[(cy, cx)][2]
			del sharks[(cy, cx)]
			break

	new_sharks = dict()

	for (y, x), (s, d, z) in sharks.items():
		ny, nx = y, x
		if d <= 1:
			cycle = (R-1) * 2
			if cycle > 0:
				ns = s % cycle
			else:
				ns = 0

			ny, nx = y, x
			for _ in range(ns):
				if not (0 <= ny + dy[d] < R):
					d ^= 1
				ny += dy[d]
		else:
			cycle = (C-1) * 2
			if cycle > 0:
				ns = s % cycle
			else:
				ns = 0

			ny, nx = y, x
			for _ in range(ns):
				if not (0 <= nx + dx[d] < C):
					d ^= 1
				nx += dx[d]

		if (ny, nx) in new_sharks:
			if z > new_sharks[(ny, nx)][2]:
				new_sharks[(ny, nx)] = (s, d, z)
		else:
			new_sharks[(ny, nx)] = (s, d, z)

	sharks = new_sharks

print(ans)