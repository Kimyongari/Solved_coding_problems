t = int(input())
for _ in range(t):
    dp = [1,1,1,2,2,3,4,5,7]
    n = int(input())
    if n<=9:
        print(dp[n-1])
    else:
        for i in range(9,n):
            dp.append(dp[i-1] + dp[i-5])
        print(dp[n-1])