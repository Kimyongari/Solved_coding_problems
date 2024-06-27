from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
arr = [list(map(int,input().split())) for _ in range(n)]
def distance(start):
    x,y = start
    global _arr, chick, n
    d = float('inf')
    for i in chick:
        _x = i // n
        _y = i % n
        d = min(d, abs(x-_x) + abs(y-_y))
    return d
answer = float('inf')
l = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            l.append(i*n+j)
for comb in combinations(l,len(l)-m):
    _arr = deepcopy(arr)
    chick = deepcopy(l)
    cnt = 0
    for a in comb:
        x = a//n
        y = a%n
        _arr[x][y] = 0
        chick.remove(a)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                cnt += distance((i,j))
    answer = min(answer, cnt)
print(answer)