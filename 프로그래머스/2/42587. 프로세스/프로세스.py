from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque((a,b) for a, b in enumerate (priorities))
    while True:
        a, b = queue.popleft()
        if any(b < i[1] for i in queue ):
            queue.append((a,b))
        else:
            answer += 1
            if a == location:
                return answer
