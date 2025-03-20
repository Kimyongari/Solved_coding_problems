n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
# 각 셀은 [가로, 세로, 대각]을 의미
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(n):
        t1,t2,t3 = 0,0,0
        if g[i][j]==0 and (i,j)!=(0,1):
            # 가로인 상태로 넘어오는 경우(노란색)
            if j>=1:
                t1 += (dp[i][j-1][0] + dp[i][j-1][2])
            # 세로인 상태로 넘어오는 경우(초록색)
            if i>=1:
                t2 += (dp[i-1][j][1] + dp[i-1][j][2])
            # 대각선인 상태로 넘어오는 경우(파란색)
            if i>=1 and j>=1:
                if g[i-1][j]!=1 and g[i][j-1]!=1:
                    t3 += sum(dp[i-1][j-1])
            dp[i][j]=[t1,t2,t3]
#         print(dp)
print(sum(dp[-1][-1]))