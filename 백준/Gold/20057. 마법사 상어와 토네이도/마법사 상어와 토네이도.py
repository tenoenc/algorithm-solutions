import sys

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [0, 1, 0, -1], [-1, 0, 1, 0]
cy, cx = N // 2, N // 2

moves = []
amount = 0

for i in range(1, N):
	for j in range(2 if i < N-1 else 3):
		nd = (2*(i-1)+j)%4
		ny, nx = cy + dy[nd] * i, cx + dx[nd] * i
		moves.append((cy, cx, nd))
		cy, cx = ny, nx

def get_adj(y, x, d):
	unp1 = (1/100, y + dy[(d+1)%4], x + dx[(d+1)%4])
	dnp1 = (1/100, y + dy[(d+3)%4], x + dx[(d+3)%4])
	unp2 = (2/100, y + dy[d] + dy[(d+1)%4] * 2, x + dx[d] + dx[(d+1)%4] * 2)
	dnp2 = (2/100, y + dy[d] + dy[(d+3)%4] * 2, x + dx[d] + dx[(d+3)%4] * 2)
	unp5 = (5/100, y + dy[d] * 3, x + dx[d] * 3)
	unp7 = (7/100, y + dy[d] + dy[(d+1)%4], x + dx[d] + dx[(d+1)%4])
	dnp7 = (7/100, y + dy[d] + dy[(d+3)%4], x + dx[d] + dx[(d+3)%4])
	unp10 = (10/100, y + dy[d] * 2 + dy[(d+1)%4], x + dx[d] * 2 + dx[(d+1)%4])
	dnp10 = (10/100, y + dy[d] * 2 + dy[(d+3)%4], x + dx[d] * 2 + dx[(d+3)%4])

	return [unp1, dnp1, unp2, dnp2, unp5, unp7, dnp7, unp10, dnp10]


def tonado(xy, xx, d):
	global amount
	yy, yx = xy + dy[d], xx + dx[d]
	ay, ax = xy + dy[d] * 2, xx + dx[d] * 2

	yval = grid[yy][yx]

	for p, y, x in get_adj(xy, xx, d):
		dval = int(grid[yy][yx] * p)
		yval -= dval
		if 0 <= y < N and 0 <= x < N:
			grid[y][x] += dval
		else:
			amount += dval

	grid[yy][yx] = 0
	if 0 <= ay < N and 0 <= ax < N:
		grid[ay][ax] += yval
	else:
		amount += yval

while moves:
	sy, sx, d = moves.pop(0)
	if moves:
		ey, ex, _ = moves[0]
	else:
		ey, ex = 0, -1

	if d == 0:
		y = sy
		for x in range(sx, ex, -1):
			tonado(y, x, d)
	elif d == 1:
		x = sx
		for y in range(sy, ey):
			tonado(y, x, d)
	elif d == 2:
		y = sy
		for x in range(sx, ex):
			tonado(y, x, d)
	else:
		x = sx
		for y in range(sy, ey, -1):
			tonado(y, x, d)

print(amount)