from itertools import combinations
from collections import deque
def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt
def solution(n,wires):
    comb = list(combinations(wires, len(wires)-1))
    answer_l = []
    for i in comb:
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        for j in i:
            a,b = j
            graph[a].append(b)
            graph[b].append(a)
        for j in graph:
            if j:
                c = bfs(graph,visited,j[0])
                other = n-c
                answer_l.append(abs(c-other))
                break
    return(min(answer_l))