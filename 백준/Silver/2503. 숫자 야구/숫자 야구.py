n = int(input())
d = []
for _ in range(n):
    d.append(input().split())

def calcul(target, answer):
    st = 0
    b = 0
    answer_set = set(answer)  # 답안을 set으로 변환하여 효율적으로 검사
    for i in range(len(target)):
        if target[i] == answer[i]:
            st += 1
        elif target[i] in answer_set:  # set을 사용하여 포함 여부 확인
            b += 1
    return st, b

cnt = 0
for first in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    for second in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        for third in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if len(set(first + second + third)) != 3: 
                continue
            target = first + second + third
            cc = 0
            for l in d:
                answer, strike, ball = l[0], l[1], l[2]
                st, b = calcul(target, answer)
                if int(strike) == st and int(ball) == b:
                    cc += 1
            if cc == len(d):  
                cnt += 1

print(cnt)
