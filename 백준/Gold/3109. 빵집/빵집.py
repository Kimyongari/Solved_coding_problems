r, c=map(int, input().split())
graph=[]
for _ in range(r):
    graph.append(list(map(str, input())))
answer=0
dy=[-1, 0, 1]
dx=[1, 1, 1]
def dfs(y, x):
    if x==c-1:
        return True
    for i in range(3):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<r and 0<=nx<c and graph[ny][nx]=='.':
            graph[ny][nx]='x'
            if dfs(ny, nx):
                return True
    return False
for i in range(r):
    if graph[i][0]=='.':
        if dfs(i, 0):
            answer+=1
print(answer)