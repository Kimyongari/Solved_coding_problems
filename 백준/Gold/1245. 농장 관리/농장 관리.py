from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]

answer = 0
visited = [[False for m in range(M)] for n in range(N)]
move = [(0, -1), (0, 1), (-1, -1), (1, -1), (-1, 0), (1, 0), (1, 1), (-1, 1)]# 모든 구역에 대해 탐색 시작

for x in range(N):
    for y in range(M):
        if visited[x][y]:
            continue
        flag = True
        q = deque()
        q.append([x,y])
        while q:
            _x, _y = q.popleft()
            visited[_x][_y] = True
            for dx,dy in move:
                _dx,_dy = _x+dx, _y+dy
                if 0 <= _dx < N and 0<= _dy < M:
                    if graph[_x][_y] == graph[_dx][_dy] and not visited[_dx][_dy]:
                        q.append([_dx, _dy])
                    elif graph[_x][_y] < graph[_dx][_dy]:
                        flag = False

        if flag:
            answer += 1
print(answer)