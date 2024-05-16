from collections import deque

move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

def DFS(table, a, b):
    queue = deque()
    queue.append(a)
    queue.append(b)
    table[a][b] = 0
    M, N = len(table), len(table[0])

    while queue:
        x = queue.popleft()
        y = queue.popleft()

        for i in range(4):
            dx = x + move_x[i]
            dy = y + move_y[i]
            if 0 <= dx < M and 0 <= dy < N and table[dx][dy] == 1:
                queue.append(dx)
                queue.append(dy)
                table[dx][dy] = 0

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    table = [[0] * N for _ in range(M)]

    for _ in range(K):
        a, b = map(int, input().split())
        table[a][b] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if table[i][j] == 1:
                DFS(table, i, j)
                count += 1

    print(count)
