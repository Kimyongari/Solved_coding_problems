def solution(triangle):
    dp = [ [] for i in range(len(triangle)+1)]
    dp[0].append(triangle[0][0])
    l = len(triangle)
    for i in range(1,l):
        for j in range(len(triangle[i])):
            if j == 0 :
                dp[i].append(dp[i-1][0] + triangle[i][0])
            elif j == len(triangle[i])-1:
                dp[i].append(dp[i-1][-1] + triangle[i][-1])
            else:
                dp[i].append(max((dp[i-1][j-1] + triangle[i][j]), 
                                dp[i-1][j] + triangle[i][j]))
    return(max(dp[l-1]))

# dp[0] : 7
# dp[1] : 10, 15
# dp[2] : 18, 11, 16, 15  ( dp[2][0] = dp[1][0] + t[2][0] 
#                           dp[2][1] = dp[1][0] + t[2][1]
#                           dp[2][1] = dp[1][1] + t[2][2]
#                           dp[2][2] = dp[1][1] + t[2][3])
# dp                          