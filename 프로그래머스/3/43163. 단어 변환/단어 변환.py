from collections import deque
def bfs(start, graph, visited, target):
    q = deque()
    q.append((start, 0))  # Tuple 형태로 현재 문자열과 변환 횟수를 함께 큐에 추가
    visited[start] = True

    while q:
        current, cnt = q.popleft()
        if current == target:
            return cnt

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, cnt + 1))

    return 0


def solution(begin, target, words):
    d = {i:[] for i in words}
    d[begin] = []
    for i in d:
        for j in words:
            cnt = sum(1 for x,y in zip(i,j) if x!=y)
            if cnt == 1:
                d[i].append(j)
    visited = {i : False for i in words}
    visited[begin] = False
    answer = bfs(begin, d, visited, target)
    return answer

