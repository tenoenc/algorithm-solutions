N = int(input())
cards = [0] + list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
	dp[i] = cards[i]
	for j in range(i):
		dp[i] = max(dp[i], dp[j] + cards[i-j])

print(dp[N])