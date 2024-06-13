from collections import deque

n, m, v = map(int, input().split())
d = {(i+1) : [] for i in range(n)}

for _ in range(m):
    a,b = map(int,input().split())
    if a not in d[b]:
        d[b].append(a)
    if b not in d[a]:
        d[a].append(b)
        
for i in range(n):
    d[i+1] = sorted(d[i+1])
    
def dfs(start, arr):
    global answer_dfs
    answer_dfs.append(start)
    visited[start] = True
    for i in arr[start]:
        if not visited[i]:
            dfs(i, arr)
    return answer_dfs
    
def bfs(start):
    global answer_bfs
    answer_bfs.append(start)
    visited[start] = True
    q = deque(d[start])
    while q:
        s = q.popleft()
        visited[s] = True
        if s not in answer_bfs:
            answer_bfs.append(s)
        for i in d[s]:
            if not visited[i]:
                q.append(i)
                
answer_dfs = []
answer_bfs = []
visited = [False] * (n+1)
dfs(v,d)
visited = [False] * (n+1)
bfs(v)
print(*answer_dfs)
print(*answer_bfs)