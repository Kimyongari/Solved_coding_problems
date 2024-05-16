from collections import deque
Q = deque()
N, K = map(int,input().split())
for i in range(1, N+1):
    Q.append(i)
answer = []
for i in range(N):
    Q.rotate(-(K-1))
    answer.append(Q.popleft())
print(f'<{", ".join(map(str, answer))}>')