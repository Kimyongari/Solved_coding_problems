from collections import deque

N = int(input())
b = deque(enumerate(map(int, input().split())))
answer = []

while b:
    idx , paper = b.popleft()
    answer.append(idx + 1)
    if paper > 0:
        b.rotate(-(paper-1))
    else:
        b.rotate(-paper)
print(' '.join(map(str,answer)))
