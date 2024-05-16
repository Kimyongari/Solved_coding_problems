def solution(tickets):
    graph = {}
    for start, end in tickets:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
    
    for key in graph:
        graph[key].sort(reverse=True)

    def bfs(start):
        stack = [start]
        path = [] 
        while stack:
            node = stack[-1]  # 현재 위치
            if node not in graph or len(graph[node]) == 0: 
                path.append(stack.pop()) 
            else:
                stack.append(graph[node].pop())  
        return path[::-1] 


    answer = bfs('ICN')
    return answer
