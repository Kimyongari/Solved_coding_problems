from collections import deque

def find_min_time(n, k):
    visited = [False] * 100001
    queue = deque([(n, 0)])
    
    while queue:
        current, time = queue.popleft()
        
        if current == k:
            return time
        
        next_positions = [current - 1, current + 1, current * 2]
        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

n, k = map(int, input().split())
print(find_min_time(n, k))
