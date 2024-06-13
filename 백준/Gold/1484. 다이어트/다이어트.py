# G = 현재제곱 - 기억제곱

g = int(input())
dp = []
for i in range(1,50001):
    dp.append(i**2)
answer = []
for i in range(len(dp)):
    for j in range(i-1,-1,-1):
        v = dp[i]-dp[j]
        if v == g:
            answer.append(dp[i]**(1/2))
            break
        elif v - g > 0:
            break
answer = list(filter(lambda x: int(x) == x, answer))
if answer:
    for i in answer:
        print(int(i))
else:
    print(-1)