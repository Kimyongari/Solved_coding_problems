import heapq
n = int(input())
start = []
q = []
end = []
for i in range(1,n+1):
    _, start, end = map(int, input().split())
    q.append([start,end])
q = sorted(q)
meanh = []
cnt = 0
for i in q:
    if meanh and meanh[0] <= i[0]:
        heapq.heappop(meanh)
    heapq.heappush(meanh, i[1])
    cnt = max(cnt, len(meanh))
print(cnt)