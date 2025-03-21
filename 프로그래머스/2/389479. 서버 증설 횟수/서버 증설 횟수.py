def solution(players, m, k):
    dp = [1] * 24
    # m : 늘어난 인원수
    # k : 운영시간
    answer = 0
    for i in range(24):
        player = players[i]
        can = dp[i] * m
        if player >= can:
            need = ((player - can) // m) + 1
            for j in range(i,min(i+k,24)):
                dp[j] += need
            answer += need
    print(list(map(lambda x: x-1,dp)))
    return answer