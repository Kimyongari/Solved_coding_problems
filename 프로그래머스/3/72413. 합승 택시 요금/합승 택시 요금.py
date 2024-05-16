def floyd(dist, n):
    for k in range(n+1):
        for start in range(n+1):
            for end in range(n+1):
                if dist[start][end] >= dist[start][k] + dist[k][end]:
                    dist[start][end] = dist[start][k] + dist[k][end]
def solution(n, s, a, b, fares):
    dist = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        dist[i][i] = 0
    for start, end, cost in fares:
        dist[start][end] = cost
        dist[end][start] = cost
    floyd(dist, n)
    answer = float('inf')
    for k in range(n+1):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])
    return answer