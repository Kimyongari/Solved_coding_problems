import heapq
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
arr = sorted(arr)
q = []
for i in arr:
    heapq.heappush(q, i[1])
    if len(q) > i[0]:
        heapq.heappop(q)
print(sum(q))