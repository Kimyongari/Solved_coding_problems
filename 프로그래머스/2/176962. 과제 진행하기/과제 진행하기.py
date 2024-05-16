from collections import deque
def solution(plans):
    answer = []
    for i in range(len(plans)):
        n, start, work = plans[i]
        h, m = start.split(':')
        plans[i][1], plans[i][2] = int(h)*60 + int(m), int(work)
    plans = sorted(plans, key = lambda x : x[1])
    works = deque()
    left_time = 0
    
    for i in range(len(plans)):
        name, start, work = plans[i]
        while works:
            _name, _work = works.pop()
            if left_time >= _work:
                left_time -= _work
                answer.append(_name)
            else:
                works.append([_name, _work - left_time])
                break
        
        works.append([name, work])
        if i < len(plans)-1:
            next_start = plans[i+1][1]
            left_time = next_start - start
    while works:
        n, _ = works.pop()
        answer.append(n)
    return answer