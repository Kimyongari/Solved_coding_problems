import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
d = {i+1 : [] for i in range(n)}
for _ in range(n-1):
    a, b = map(int, input().split())
    if b not in d[a]:
        d[a].append(b)
    if a not in d[b]:
        d[b].append(a)

q = deque([1])
visited = [0] * (n+1)
while q:
    s = q.popleft()
    for j in d[s]:
        if visited[j] == 0:
            visited[j] = s
            q.append(j)
for i in range(2,n+1):
    print(visited[i])
