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
		if d <= 1:
			if R > 1:
				cycle = (R-1) * 2
			
				if d == 0:
					dist = cycle - y
				else:
					dist = y

				dist = (dist + s) % cycle

				if dist < R:
					ny, nd = dist, 1
				else:
					ny, nd = cycle - dist, 0
			else:
				ny, nd = y, d

			nx = x
		else:
			if C > 1:
				cycle = (C-1) * 2

				if d == 3:
					dist = cycle - x
				else:
					dist = x

				dist = (dist + s) % cycle

				if dist < C:
					nx, nd = dist, 2
				else:
					nx, nd = cycle - dist, 3
			else:
				nx, nd = x, d

			ny = y


		if (ny, nx) in new_sharks:
			if z > new_sharks[(ny, nx)][2]:
				new_sharks[(ny, nx)] = (s, nd, z)
		else:
			new_sharks[(ny, nx)] = (s, nd, z)

	sharks = new_sharks

print(ans)