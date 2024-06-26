from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    q = deque(l)
    cnt = 0
    answer = 0
    while q:
        maxi = max(q)        
        a = q.popleft()        
        if a == maxi and m == 0:
            answer = cnt + 1
            break
        elif a != maxi and m == 0:
            q.append(a)
            m = len(q) - 1
        elif a == maxi and m != 0:
            cnt += 1
            m -= 1
        else:
            q.append(a)
            m -= 1
    print(answer)
        