from collections import deque
import sys

Q = deque([])
N = int(sys.stdin.readline())
for _ in range(N):
    order = sys.stdin.readline()
    if order.find('push ')== 0:
        Q.append(int(order[5:]))
    if order.find('pop') == 0:
        if len(Q) == 0:
            print(-1)
        else:
            a = Q.popleft()
            print(a)
    if order.find('size') == 0:
        print(len(Q))
    if order.find('empty') == 0:
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    if order.find('front') == 0:
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    if order.find('back') == 0:
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])