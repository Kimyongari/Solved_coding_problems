from collections import deque
n = int(input())
q = deque((range(1,n+1)))
if n == 1:
    print(1)
else:
    while q:
        q.popleft()
        if len(q) == 1:
            break
        else:
            q.append(q.popleft())
    print(q[0])