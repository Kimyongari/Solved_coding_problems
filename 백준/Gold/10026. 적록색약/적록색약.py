from collections import deque
n = int(input())

arr1 = []
arr2 = []
for _ in range(n):
    box = input()
    arr1.append(list(box))
    arr2.append(list(box.replace('R','G')))
    

def check(q, arr, target):
    q = deque([q])
    while q:
        x,y = q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            _dx,_dy = x+dx, y+dy   
            if 0<=_dx<n and 0<=_dy<n and arr[_dx][_dy] == target:
                arr[_dx][_dy] = 'O'
                q.append((_dx,_dy))
    return arr
cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if arr1[i][j] != 'O':
            arr1 = check((i,j), arr1, arr1[i][j])
            cnt1 += 1
        if arr2[i][j] != 'O':
            arr2 = check((i,j), arr2, arr2[i][j])
            cnt2 += 1

print(cnt1, cnt2)
