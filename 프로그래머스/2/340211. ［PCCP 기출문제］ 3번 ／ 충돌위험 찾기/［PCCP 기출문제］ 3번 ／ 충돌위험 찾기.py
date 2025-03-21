from collections import deque
def solution(points, routes):
    d = {i+1 : point for i,point in enumerate(points)}
    moves = [[] for i in range(len(routes))]
    robots = len(routes)
#   r좌표가 변하는 이동을 c보다 먼저
    for i,route in enumerate(routes):
        for j in range(len(route)-1):
            start = d[route[j]]
            end = d[route[j+1]]
            if j == 0:
                moves[i].append(start)
            while start != end:
                if start[0] != end[0]:
                    if end[0]-start[0]>0:
                        start = [start[0]+1, start[1]]
                        moves[i].append(start)
                    else:
                        start = [start[0]-1,start[1]]
                        moves[i].append(start)
                else:
                    if end[1]-start[1]>0:
                        start = [start[0], start[1]+1]
                        moves[i].append(start)
                    else:
                        start = [start[0], start[1]-1]
                        moves[i].append(start)
    maxday = max([len(moves[i]) for i in range(robots)])
    inters = [[] for _ in range(maxday)]
    answer = 0
    for i in range(robots):
        for i,m in enumerate(moves[i]):
            inters[i].append(m)
    for day in inters:
        day = deque(day)
        ll = []
        while day:
            a = day.popleft()
            if a in day and a not in ll:
                ll.append(a)
        answer += len(ll)
        
        
    return answer