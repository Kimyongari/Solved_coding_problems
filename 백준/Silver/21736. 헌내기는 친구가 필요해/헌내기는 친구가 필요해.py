from collections import deque

n,m = map(int, input().split())
arr = []
for i in range(n):
    infor = input()
    arr.append(infor)
    if infor.find('I') != -1:
        start = [(i, infor.find('I'))]
q = deque(start)
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0
x,y = start[0]
visited[x][y] = True
while q:
    x,y = q.popleft()
    if arr[x][y] == 'P':
        answer += 1
    for dx,dy in [(-1,0), (0,1), (1,0), (0,-1)]:
        _dx, _dy = x+dx, y+dy
        if 0<=_dx<n and 0<=_dy<m and arr[_dx][_dy] != 'X' and not visited[_dx][_dy]:
            q.append((_dx,_dy))
            visited[_dx][_dy] = True
print(answer) if answer != 0 else print('TT')
