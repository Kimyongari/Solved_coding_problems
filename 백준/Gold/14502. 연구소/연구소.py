from copy import deepcopy
from collections import deque
from itertools import combinations
def swarm(start):
    q = deque([start])
    global _m,m,n
    movement = [(0,1), (1,0), (-1,0), (0,-1)]
    while q:
        x,y = q.popleft()
        for move in movement:
            dx, dy = move
            _dx, _dy = x+dx, y+dy
            if 0 <= _dx < n and 0 <= _dy < m:
                if _m[_dx][_dy] == 0:
                    _m[_dx][_dy] = 2
                    q.append((_dx,_dy))

n, m = map(int, input().split())
arr = deque()

for _ in range(n):
    arr.append(list(map(int, input().split())))
answer = 0
l = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            l.append(i*m + j)
for comb in combinations(l,3):
    a,b,c = comb
    _m = deepcopy(arr)
    cnt = 0
    _m[a//m][a%m] = 1
    _m[b//m][b%m] = 1
    _m[c//m][c%m] = 1
    for i in range(n):
        for j in range(m):
            if _m[i][j] == 2:
                swarm((i,j))
    for i in _m:
        cnt += i.count(0)
    if cnt == 8:
        best = _m
    answer = max(answer, cnt)
print(answer)