from collections import deque
t = int(input())
d = {i : [] for i in range(t)}
for i in range(t):
    info = list(map(int, input().split()))
    for j in range(t):
        if info[j] == 1:
            d[i].append(j)

for i in range(t):
    q = deque(d[i])
    answer = [0 for i in range(t)]
    if q:
        while q:
            next = q.popleft()
            answer[next] = 1
            for i in d[next]:
                if answer[i] != 1:
                    q.append(i)
    print(*answer)

