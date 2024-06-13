n = int(input())
l = list(map(int, input().split()))
m = []
for i in range(2, 1001):
    cnt = 0
    for j in range(1, round(i**(1/2))+1,1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        m.append(i)
answer = 0
for i in l:
    if i in m:
        answer += 1

print(answer)