import sys
input = sys.stdin.readline
import heapq
l = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if l:
            print(-heapq.heappop(l))
        else:
            print(0)
    else:
        heapq.heappush(l, -x)