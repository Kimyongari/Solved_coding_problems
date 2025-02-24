from heapq import heappop, heappush
import sys
input = sys.stdin.readline
q = []
for _ in range(int(input())):
    n = int(input())
    if n != 0:
        if n > 0:
            heappush(q,[n,1])
        if n < 0:
            heappush(q, [abs(n),-1])
    if n == 0:
        if q:
            a,b = heappop(q)
            print(a*b)
        else:
            print(0)