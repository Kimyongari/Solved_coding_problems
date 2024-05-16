def solution(today, terms, privacies):
    t = {}
    answer = []
    for i in terms:
        t[i[0]] = int(i[1:]) * 28
    today = caldate(today)
    print(today)
    for i in range(len(privacies)):
        d = caldate(privacies[i][:10])
        d += t[privacies[i][11:]]
        if d <= today:
            answer.append(i+1)
        print(d)
    return answer
def caldate(date):
    y = int(date[2:4])
    m = int(date[5:7])
    d = int(date[8:])
    day = (y * (28*12)) + ((m-1) * 28) + d
    return day
