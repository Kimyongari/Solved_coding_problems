from collections import deque
import sys
input = sys.stdin.readline
def ddijkstra(graph, start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    q = deque()
    q.append([start, distances[start]])
    while q:
        s, current_d = q.popleft()
        for new_d, new_l in graph[s].items():
            new_distance = current_d + new_l
            if new_distance < distances[new_d]:
                distances[new_d] = new_distance
                q.append([new_d, new_distance])
    return distances
N, M, X = map(int, input().split())
graph = {i : {} for i in range(1,N+1)}
for i in range (M):
    s, e, t = map(int, input().split())
    graph[s][e] = t
    

answer = []
tohome = ddijkstra(graph, X)
for i in graph:
    answer.append(ddijkstra(graph,i)[X] + tohome[i])
print(max(answer))