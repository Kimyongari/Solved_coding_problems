from collections import deque
import sys
n,m = map(int, input().split())
q = []
for _ in range(n):
    pi, li = map(int, input().split())
    l = list(map(int, input().split()))
    l = sorted(l)
    if pi >= li:
        q.append(l[pi-li])
    else:
        q.append(1)

answer = 0
q = deque(sorted(q))
while q:
    cost = q.popleft()
    if cost <= m:
        m -= cost
        answer += 1
    else:
        break

print(answer)