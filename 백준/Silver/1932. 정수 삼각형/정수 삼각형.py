n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i] = list(map(int, input().split())) + ([0] * (n-(i+1)))
if n == 1:
    print(dp[0][0])
else:
    dp[1][0] = dp[0][0]+dp[1][0]
    dp[1][1] = dp[0][0]+dp[1][1]
    for i in range(2,n):
        for j in range(n):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j]
            elif 0 < j < i:
                dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j]
                
    
    print(max(dp[-1]))