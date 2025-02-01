from collections import deque

arr = []
n,m = map(int,input().split())
func = lambda x: float('inf') if x == '1' else 0
for i in range(n):
    arr.append(list(map(func, list(input()))))

start = [(0,0)]
arr[0][0] = 1
q = deque(start)
visited = [[False for _ in range(m)] for j in range(n)]
visited[0][0] = True
if arr == [[1]]:
    print(1)
else: 
    while q:
        x,y = q.popleft()
        cost = arr[x][y]
        for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            _dx = x+dx
            _dy = y+dy
            if 0<=_dx<n and 0<=_dy<m and arr[_dx][_dy] != 0 and visited[_dx][_dy] == False:
                arr[_dx][_dy] = min(cost+1, arr[_dx][_dy])
                visited[_dx][_dy] = True
                q.append((_dx,_dy))
                if _dx == n-1 and _dy == m-1:
                    print(arr[_dx][_dy])
                    q.clear()