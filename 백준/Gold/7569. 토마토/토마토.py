from collections import deque
            
def check(boxs):
    for i in boxs:
        for j in i:
            for z in j:
                if z == 0:
                    return True
    return False

def oneday(q, boxs):
    q = deque(q)
    next_q = []
    while q:
        h_idx,y,x = q.popleft()
        for dh,dy,dx in (1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1):
            _dh, _dy, _dx = h_idx+dh,y+dy,x+dx
            if 0<=_dh<h and 0<=_dy<n and 0<=_dx<m and boxs[_dh][_dy][_dx] == 0:
                boxs[_dh][_dy][_dx] = 1
                next_q.append((_dh,_dy,_dx))
    return next_q, boxs

m,n,h = list(map(int, input().split()))
q = []
boxs = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        arr = list(map(int, input().split()))
        boxs[i].append(arr)
        for z in range(m):
            if arr[z] == 1:
                q.append((i,j,z))

answer = 0
while check(boxs):
    q, boxs = oneday(q,boxs)
    if not q:
        answer = -1
        break
    answer += 1

print(answer)