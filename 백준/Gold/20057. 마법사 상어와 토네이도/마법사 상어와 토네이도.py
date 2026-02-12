import sys

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [0, 1, 0, -1], [-1, 0, 1, 0]
cy, cx = N // 2, N // 2

left_spread = [
	(-1, 0, 0.01), (1, 0, 0.01), (-1, -1, 0.07), (1, -1, 0.07),
    (-2, -1, 0.02), (2, -1, 0.02), (-1, -2, 0.1), (1, -2, 0.1),
    (0, -3, 0.05)
]

spreads = [left_spread]

for i in range(3):
	new_spread = []
	for y, x, ratio in spreads[-1]:
		new_spread.append((-x, y, ratio))
	spreads.append(new_spread)

moves = []

for i in range(1, N):
	for j in range(2 if i < N-1 else 3):
		nd = (2*(i-1)+j)%4
		ny, nx = cy + dy[nd] * i, cx + dx[nd] * i
		moves.append((cy, cx, nd))
		cy, cx = ny, nx

ans = 0

def tonado(xy, xx, d):
	global ans
	yy, yx = xy + dy[d], xx + dx[d]
	ay, ax = xy + dy[d] * 2, xx + dx[d] * 2

	yval = grid[yy][yx]

	for dy_s, dx_s, ratio in spreads[d]:
		ny, nx = xy + dy_s, xx + dx_s
		dval = int(grid[yy][yx] * ratio)
		yval -= dval
		if 0 <= ny < N and 0 <= nx < N:
			grid[ny][nx] += dval
		else:
			ans += dval

	grid[yy][yx] = 0
	if 0 <= ay < N and 0 <= ax < N:
		grid[ay][ax] += yval
	else:
		ans += yval

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

print(ans)