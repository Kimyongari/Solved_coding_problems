def change(time):
    s = str(time)
    if len(s) == 4:
        hour = s[:2]
        minute = s[2:]
        return int(hour)* 60 + int(minute)
    else:
        hour = s[:1]
        minute = s[1:]
        return int(hour)*60 + int(minute)
    
def solution(schedules, timelogs, startday):
    # 1: 월
    l = []
    for i in range(1,8):
        if startday == 6 or startday == 7:
            l.append(False)
        else:
            l.append(True)
        startday = startday%7
        startday += 1
    answer = 0
    for i in range(len(schedules)):
        timelog = list(map(change, timelogs[i]))
        deadline = change(schedules[i]) + 10
        flag = True
        for j in range(7):
            if l[j] and timelog[j] > deadline:
                flag = False
                break
        if flag:
            answer += 1
    return answer