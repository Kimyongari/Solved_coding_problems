from collections import deque

def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        current_node = q.popleft()

        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

    return visited

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                graph[i].append(j)

    for i in range(n):
        if not visited[i]:
            visited = bfs(graph, i, visited)
            answer += 1

    return answer