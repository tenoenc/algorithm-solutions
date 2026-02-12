import sys
from collections import deque

input = sys.stdin.readline

N, M, F = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ty, tx = map(int, input().split())
ty -= 1
tx -= 1

passengers = {}
for _ in range(M):
    sy, sx, ey, ex = map(int, input().split())
    passengers[(sy-1, sx-1)] = (ey-1, ex-1)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs_distance(y, x):
    visited = [[-1] * N for _ in range(N)]
    q = deque([(y, x)])
    visited[y][x] = 0
    
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] == 0 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[cy][cx] + 1
                q.append((ny, nx))
    return visited

for _ in range(M):
    dist_table = bfs_distance(ty, tx)
    candidates = []
    
    for (sy, sx) in passengers:
        dist = dist_table[sy][sx]
        if dist != -1:
            candidates.append((dist, sy, sx))
    
    if not candidates:
        print(-1)
        exit(0)
    
    candidates.sort()
    dist_to_start, sy, sx = candidates[0]
    
    if F < dist_to_start:
        print(-1)
        exit(0)
    
    F -= dist_to_start
    ty, tx = sy, sx
    
    ey, ex = passengers[(sy, sx)]
    del passengers[(sy, sx)]
    
    dist_table = bfs_distance(ty, tx)
    dist_to_end = dist_table[ey][ex]
    
    if dist_to_end == -1 or F < dist_to_end:
        print(-1)
        exit(0)
        
    F -= dist_to_end
    F += dist_to_end * 2
    ty, tx = ey, ex

print(F)