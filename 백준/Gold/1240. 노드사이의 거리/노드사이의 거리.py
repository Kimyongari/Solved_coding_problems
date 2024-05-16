from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x, 0))

    visit = [0 for _ in range(N + 1)]
    visit[x] = 'visited'

    while queue:
        cur, cur_d = queue.popleft()
        if cur == y:
            return cur_d
        for nei, dist in arr[cur]:
            if visit[nei] == 0:
                visit[nei] = 'visited'
                queue.append((nei,cur_d + dist))
                
N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
answer = []

for _ in range(N - 1):
    a, b, c = map(int,input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

for _ in range(M):
    a, b = map(int, input().split())
    answer.append((bfs(a, b)))
for i in answer:
    print(i)
            