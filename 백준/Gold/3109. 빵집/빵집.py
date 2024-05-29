import sys
input = sys.stdin.readline
r, c = map(int, input().split())
m = []
for _ in range(r):
    m.append(list(input()))

answer = 0
move = [(-1,1), (0,1), (1,1)]
def dfs(x,y):
    if y == c-1:
        return True
    for dx, dy in move:
        _x = x + dx
        _y = y + dy
        if 0 <= _x < r and 0 <= _y < c and m[_x][_y] == '.':
            m[_x][_y] = 'x'
            if dfs(_x, _y):
                return True

    return False
for i in range(r):
    if m[i][0] == '.':
        if dfs(i, 0):
            answer += 1

print(answer)
            