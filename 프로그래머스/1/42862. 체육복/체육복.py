def solution(n, lost, reserve):
    new_lost = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            new_lost.append(i)
    lost = new_lost
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    while lost:
        a = lost.pop(0)
        if a-1 in reserve:
            reserve.remove(a-1)
            answer += 1
        elif a+1 in reserve:
            reserve.remove(a+1)
            answer += 1
    return answer
