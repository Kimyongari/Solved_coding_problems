import heapq
n = int(input())
l = []
answer = 0
for _ in range(n):
    l.append(int(input()))
heapq.heapify(l)

while l:
    if len(l) == 1:
        break
    a = heapq.heappop(l)
    b = heapq.heappop(l)
    answer += (a + b)
    heapq.heappush(l, a+b)
    
print(answer)