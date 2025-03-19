from collections import deque
def L(x):
    return x*10%10000 + x//1000
def R(x):
    return x//10 + x%10*1000

def D(x):
    x = int(x)
    x *= 2
    return x%10000

def S(x):
    x = int(x)
    if x == 0:
        return 9999
    else:
        return x-1



t = int(input())
for _ in range(t):
    visited = [False]*10001
    start, target = map(int, input().split())
    visited[start] = True
    q = deque([(start, '')])
    while q:
        now,answer = q.popleft()
        next1 = D(now)
        next2 = S(now)
        next3 = L(now)
        next4 = R(now)
        if not visited[next1]:
            if next1 == target:
                print(answer + 'D')
                break
            visited[next1] = True
            q.append((next1, answer + 'D'))
        if not visited[next2]:
            if next2 == target:
                print(answer + 'S')
                break
            visited[next2] = True
            q.append((next2, answer + 'S'))
        if not visited[next3]:
            if next3 == target:
                print(answer + 'L')
                break
            visited[next3] = True
            q.append((next3, answer + 'L'))
        if not visited[next4]:
            if next4 == target:
                print(answer + 'R')
                break
            visited[next4] = True
            q.append((next4, answer + 'R'))
