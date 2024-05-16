
def solution(bridge_length, weight, truck_weights):
    bdg = []
    now = []
    sums = []
    time = 0
    for i in truck_weights:
        bdg.append(i)
    a = bdg.pop(0)
    now.append([a,0])
    sums.append(a)
    while now:
        time += 1
        for i in range(len(now)):
            now[i][1] += 1
        if now[0][1] >= bridge_length:
            now.pop(0)
            sums.pop(0)

        if bdg:
            if sum(sums) + bdg[0] <= weight:
                a = bdg.pop(0)
                now.append([a,0])
                sums.append(a)
        if now:
            continue
    time += 1
    return time