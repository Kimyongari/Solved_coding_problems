from collections import deque
arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
arr = deque(arr)
l = deque([i+1 for i in range(n)])
answer = []
t = []
while l:
    t.append(l.popleft())
    answer.append('+')
    while t[-1] == arr[0]:
        arr.popleft()
        t.pop()
        answer.append('-')
        if not arr or not t:
            break
if arr:
    print('NO')
else:
    for i in answer:
        print(i)
