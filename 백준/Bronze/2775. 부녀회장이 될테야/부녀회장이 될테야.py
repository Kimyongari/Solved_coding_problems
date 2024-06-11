t = int(input())
for _ in range(t):
    k = int(input()) # 2 층
    n = int(input()) # 3 호
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(n+1):
        dp[0][i] = i
    for i in range(1,k+1):
        for j in range(n+1):
            dp[i][j] = sum(dp[i-1][:(j+1)])
    print(dp[k][n])