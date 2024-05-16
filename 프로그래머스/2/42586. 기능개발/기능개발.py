def solution(progresses, speeds):
    days = 0
    cnt = 0
    answer = []
    d = {}
    l = []

    while len(progresses) > 0:
        a = progresses[0]
        b = speeds[0]
        if a + (b*days) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            answer.append(days)
        else:
            days += 1
    for i in answer:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in d:
        l.append(d[i])
    return l