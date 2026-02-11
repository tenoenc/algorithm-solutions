from collections import deque

F, S, G, U, D = map(int, input().split())

queue = deque([[S, 0]])
visited = [False] * (F+1)
visited[S] = True

while queue:
	f, cnt = queue.popleft()

	if f == G:
		print(cnt)
		exit(0)

	for df in [U, -D]:
		nf = f + df
		if 1 <= nf <= F and not visited[nf]:
			visited[nf] = True
			queue.append([nf, cnt+1])

print("use the stairs")