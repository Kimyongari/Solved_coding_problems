import sys
from heapq import heappop, heappush
input = sys.stdin.readline

t = int(input())
for i in range(t):
    minq = []
    maxq = []
    nums = {}
    k = int(input())
    for j in range(k):
        order, n = input().split()
        n = int(n)

        if order == 'I':
            if n in nums:
                nums[n] += 1
                heappush(minq, n)
                heappush(maxq, -n)
            else:
                nums[n] = 1
                heappush(minq, n)
                heappush(maxq, -n)
        if order == 'D':
            if nums:
                if n == 1:
                    while -maxq[0] not in nums:
                        t = -heappop(maxq)
                    t = -heappop(maxq)
                    nums[t] -= 1
                    if nums[t] == 0:
                        del nums[t]
                if n == -1:
                    while minq[0] not in nums:
                        t = heappop(minq)
                    t = heappop(minq)
                    nums[t] -= 1
                    if nums[t] == 0:
                        del nums[t]
    if not nums:
        print('EMPTY')
    else:
        while -maxq[0] not in nums:
            heappop(maxq)
        while minq[0] not in nums:
            heappop(minq)
        print(-maxq[0], minq[0])