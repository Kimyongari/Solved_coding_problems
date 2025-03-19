from collections import deque
from collections import defaultdict
start, target = map(int, input().split())
def double(x):
    return x*2
def add(x):
    return x*10+1

q = deque([(start, 0)])
flag = False
while q:
    now,cnt = q.popleft()
    next1 = double(now)
    next2 = add(now)
    if next1 == target or next2 == target:
        print(cnt +2)
        flag = True
        break
    if next1 < target:
        q.append((next1, cnt+1))
    if next2 < target:
        q.append((next2, cnt+1))

if not flag:
    print(-1)