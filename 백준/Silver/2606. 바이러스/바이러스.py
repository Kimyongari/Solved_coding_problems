n = int(input())
d = {i+1 : [] for i in range(n)}
for _ in range(int(input())):
    a,b = map(int, input().split())
    if a not in d[b]:
        d[b].append(a)
    if b not in d[a]:
        d[a].append(b)
        
def dfs(start, d):
    global visited
    visited[start] = 1
    for i in d[start]:
        if visited[i] == 0:
            dfs(i, d)

visited = [0] * (n+1)
dfs(1, d)
print(sum(visited)-1)