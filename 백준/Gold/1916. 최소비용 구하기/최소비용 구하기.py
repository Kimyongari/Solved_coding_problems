from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
cities = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    cities[start].append([cost, end])

costs = [ float('inf') for _ in range(n+1)]
heap = []
start, end = map(int, input().split())
costs[start] = 0
heappush(heap, [costs[start], start])

while heap:
    cost, v = heappop(heap)
    if v == end:
        break
    for next_cost, next_end in cities[v]:
        if cost+next_cost < costs[next_end]:
            costs[next_end] = min(costs[next_end], cost + next_cost)
            heappush(heap, [costs[next_end], next_end])

print(costs[end])