from heapq import *
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == 1:
                maps[x][y] = float("inf")
    h = []
    q = (0,0,1)
    heappush(h,q)
    answer = 0
    while h:
        cx,cy,cv = heappop(h)
        for x,y in (0,-1),(0,1),(1,0),(-1,0):
            dx,dy = cx + x, cy + y
            if dx in range(n) and dy in range(m) and maps[dx][dy] != 0: 
                if cv + 1 < maps[dx][dy]:
                    maps[dx][dy] = cv + 1
                    heappush(h, (dx,dy,cv + 1))
    for line in maps:
        print(line)
    return maps[n-1][m-1] if maps[n-1][m-1] != float("inf") else -1