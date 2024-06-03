import heapq
def solution(n, k, enemy):
    answer = 0
    q = []
    if k >= len(enemy):
        return len(enemy)
    for i in range(len(enemy)):
        heapq.heappush(q, enemy[i])
        if len(q) > k:
            a = heapq.heappop(q)
            n -= a
            if n == 0:
                return i + 1
            if n < 0:
                return i
    return len(enemy)
