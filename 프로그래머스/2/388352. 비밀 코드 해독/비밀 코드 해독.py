from itertools import combinations

def solution(n, q, ans):
    can = [i+1 for i in range(n)]
    answer_l = []
    for comb in combinations(can,5):
        s1 = set(comb)
        flag = True
        for i in range(len(q)):
            s2 = set(q[i])
            if len(s1.intersection(s2)) != ans[i]:
                flag = False
                break
        if flag:
            answer_l.append(comb)
    answer = len(answer_l)
    
    return answer