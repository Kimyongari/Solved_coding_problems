t = int(input())
for _ in range(t):
    l = []
    n = int(input())
    l.append(list(map(int, input().split())))
    l.append(list(map(int, input().split())))
    dp = [[0 for _ in range(n)] for _ in range(2)]

    dp[0][0] = l[0][0]
    dp[1][0] = l[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    dp[0][1] = l[1][0] + l[0][1]
    dp[1][1] = l[0][0] + l[1][1]
    
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-2] + l[0][i], dp[1][i-1] + l[0][i])
        dp[1][i] = max(dp[0][i-2] + l[1][i], dp[0][i-1] + l[1][i])
    print(max(dp[1][-1], dp[0][-1]))