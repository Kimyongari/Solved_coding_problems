def solution(citations):
    answer = []
    for i in range(0,max(citations) + 1):
        cnt = 0
        for j in citations:
            if i <= j:
                cnt += 1
        if cnt >= i :
            answer.append(i)
    return max(answer)