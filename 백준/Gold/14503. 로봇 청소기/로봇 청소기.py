from collections import deque
n,m = map(int, input().split())
r,c,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
movement = {0 : (-1,0), 1 : (0,1), 2 : (1,0), 3 : (0,-1)}
start = (r,c)
q = deque()
q.append(start)
answer = 0
while q:
    x,y = q.popleft()
    cnt = 0
    if arr[x][y] == 0:
        arr[x][y] = 2
        answer += 1
    for move in movement:
        _x,_y =  movement[move]
        _x,_y = x+_x, y+_y
        if 0<=_x<n and 0<=_y<m and arr[_x][_y] == 0: # 청소되지 않은 칸이 있다면
            cnt += 1
    if cnt == 0: # 청소되지 않은 칸이 없다면
        _x, _y = movement[(d-2) % 4]
        _x, _y = x+_x, y+_y
        if 0<=_x<n and 0<=_y<m and arr[_x][_y] != 1:
            q.append((_x,_y))
        elif 0<=_x<n and 0<=_y<m and arr[_x][_y] == 1:
            break
    elif cnt != 0: # 청소되지 않은 칸이 있다면 
        for i in range(4):
            d = (d-1)%4
            _x, _y = movement[d]
            _x, _y = x+_x, y+_y
            if 0<=_x<n and 0<=_y<m and arr[_x][_y] == 0:
                q.append((_x,_y))
                break
print(answer)
