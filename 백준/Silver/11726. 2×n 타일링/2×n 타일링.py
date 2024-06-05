n = int(input())
dp = [1 for _ in range(n+1)]
if n == 1:
    print(dp[1])
else:
    dp[2] = 2
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[n]%10007)