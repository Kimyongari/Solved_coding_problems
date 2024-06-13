
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0
def check(x,y,N):
    global w, b
    cnt = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            if m[i][j] == 1:
                cnt += 1
    if cnt == 0:
        w += 1
        
    elif cnt == N ** 2:
        b += 1
        
    else:
        check(x, y, N//2)
        check(x+(N//2), y, N//2)
        check(x, y+(N//2), N//2)
        check(x+(N//2), y+(N//2), N//2)

check(0,0,n)
print(w)
print(b)
