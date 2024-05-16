def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_o = 0
    b_o = 0
    c_o = 0
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            a_o += 1
        if answers[i] == b[i%16]:
            b_o += 1
        if answers[i] == c[i%10]:
            c_o += 1
    d = []
    d.append(a_o)
    d.append(b_o)
    d.append(c_o)
    m = max(d)
    answer = []
    for i in range(len(d)):
        if d[i] == m:
            answer.append(i+1)

    return answer
