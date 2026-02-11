def solution(m, n, puddles):
    puddles_set = set()
    
    for x, y in puddles:
        puddles_set.add((y, x))
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        if (i, 1) in puddles_set:
            break
        dp[i][1] = 1
    
    for i in range(1, m+1):
        if (1, i) in puddles_set:
            break
        dp[1][i] = 1
    
    for i in range(2, n+1):
        for j in range(2, m+1):
            if (i, j) not in puddles_set:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
    return dp[n][m]