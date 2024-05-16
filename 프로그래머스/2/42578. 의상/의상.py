def solution(clothes):
    d = {}
    for i in clothes:
        if i[1] not in d:
            d[i[1]] = []
            d[i[1]].append(i[0])
        else:
            d[i[1]].append(i[0])
    answer = 1
    for i in d:
        answer *= len(d[i]) + 1
        
    answer = answer - 1
    return answer
            