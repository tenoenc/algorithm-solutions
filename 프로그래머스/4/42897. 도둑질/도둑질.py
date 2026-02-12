def solution(money):
    n = int(len(money))
    # dp[i]: i번째 집까지 고려했을 때, 훔칠 수 있는 돈의 최댓값
    
    # 첫 집을 터는 경우, 마지막 집은 못 텀
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(max(dp1), max(dp2))