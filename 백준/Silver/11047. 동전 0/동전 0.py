from collections import deque
n, target = map(int,input().split())
coins = deque()
for i in range(n):
    coins.append(int(input()))

coins = deque(filter(lambda x:x<=target, coins))
cnt = 0
while target != 0:
    a = coins.pop()
    cnt += target // a
    target %= a

print(cnt)