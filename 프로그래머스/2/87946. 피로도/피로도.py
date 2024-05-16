from itertools import permutations
def solution(k, dungeons):
    answer = []
    l = []
    for i in range(1, len(dungeons)+1):
        a = list(permutations(dungeons, i))
        for i in a:
            l.append(i)
    for i in l:
        result = 0 
        now = k
        for j in i:
            a,b = j
            if now >= a:
                now -= b
                result += 1
        answer.append(result)
    return max(answer)