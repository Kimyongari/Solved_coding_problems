n = int(input())
arr = []
cities = 0
for _ in range(n):
    arr.append(list(input()))
def dfs(start):
    global cities
    x,y = start
    arr[x][y] = '0'
    cities += 1
    for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        _dx, _dy = x+dx, y+dy
        if 0<=_dx<n and 0<=_dy<n and arr[_dx][_dy] == '1':
            dfs((_dx,_dy))
answer = []
for x in range(n):
    for y in range(n):
        if arr[x][y] == '1':
            dfs((x,y))
            answer.append(cities)
            cities = 0
print(len(answer))
answer.sort()
for i in answer:
    print(i)
            