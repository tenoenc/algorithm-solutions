import sys

input = sys.stdin.readline
N = int(input())
grid = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

total_people = sum(sum(row) for row in grid)

def solve(x, y, d1, d2):
    counts = [0] * 5
    
    is_border = [[False] * (N + 1) for _ in range(N + 1)]
    
    for i in range(d1 + 1):
        is_border[x + i][y - i] = True
        is_border[x + d2 + i][y + d2 - i] = True
    for i in range(d2 + 1):
        is_border[x + i][y + i] = True
        is_border[x + d1 + i][y - d1 + i] = True
        
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if is_border[r][c]: break
            counts[0] += grid[r][c]
            
    for r in range(1, x + d2 + 1):
        for c in range(N, y, -1):
            if is_border[r][c]: break
            counts[1] += grid[r][c]
            
    for r in range(x + d1, N + 1):
        for c in range(1, y - d1 + d2):
            if is_border[r][c]: break
            counts[2] += grid[r][c]
            
    for r in range(x + d2 + 1, N + 1):
        for c in range(N, y - d1 + d2 - 1, -1):
            if is_border[r][c]: break
            counts[3] += grid[r][c]
            
    counts[4] = total_people - sum(counts)
    
    return max(counts) - min(counts)

answer = float('inf')

for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                if x + d1 + d2 <= N and 1 <= y - d1 and y + d2 <= N:
                    answer = min(answer, solve(x, y, d1, d2))

print(answer)