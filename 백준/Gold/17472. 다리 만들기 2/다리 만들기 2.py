import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

island_num = 1
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            q = deque([(i, j)])
            visited[i][j] = True
            grid[i][j] = island_num
            while q:
                y, x = q.popleft()
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and grid[ny][nx] == 1:
                        visited[ny][nx] = True
                        grid[ny][nx] = island_num
                        q.append((ny, nx))
            island_num += 1

num_islands = island_num - 1

edges = []

def get_bridges(y, x, s_num):
    for d in range(4):
        dist = 0
        ny, nx = y + dy[d], x + dx[d]
        while 0 <= ny < N and 0 <= nx < M:
            if grid[ny][nx] == s_num: # 같은 섬이면 중단
                break
            if grid[ny][nx] == 0: # 바다라면 다리 연장
                dist += 1
                ny += dy[d]
                nx += dx[d]
            else: # 다른 섬을 만났다면
                if dist >= 2: # 다리 길이는 2 이상이어야 함
                    edges.append((dist, s_num, grid[ny][nx]))
                break

for i in range(N):
    for j in range(M):
        if grid[i][j] > 0:
            get_bridges(i, j, grid[i][j])

# 간선을 다리 길이순으로 정렬
edges.sort()

parent = [i for i in range(num_islands + 1)]

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA, rootB = find(a), find(b)
    if rootA != rootB:
        parent[rootB] = rootA
        return True
    return False

ans = 0
bridge_count = 0
for w, u, v in edges:
    if union(u, v):
        ans += w
        bridge_count += 1

# 모든 섬을 연결하는 다리의 개수는 (섬의 개수 - 1)이어야 함
if bridge_count == num_islands - 1:
    print(ans)
else:
    print(-1)