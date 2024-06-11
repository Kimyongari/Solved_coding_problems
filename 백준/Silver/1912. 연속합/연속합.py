n = int(input())
l = list(map(int, input().split()))
if max(l) < 0:
    print(max(l))
else:
    dp = [0] * (n+1)
    for i in range(n):
        dp[i+1] = max(0, dp[i]+l[i])
    print(max(dp))