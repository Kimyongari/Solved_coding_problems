import sys
from heapq import heappush, heappop
input = sys.stdin.readline
q = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if not q:
            print(0)
        else:
            print(heappop(q))
    else:
        heappush(q, n)