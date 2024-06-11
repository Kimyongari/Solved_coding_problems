n = int(input())
dp = [[0] * (n+1) for _ in range(2)]
ok = False
for i in range(3,(n+1),3):
    dp[0][i] = 1

if n%5 == 0:
    print(n//5)
    ok = True
else:
    for i in range(5,(n+1),5):
        dp[1][i] = 1
    
    for i in range(0, n+1):
        if dp[0][i] + dp[1][n-i] == 2:
            print((n-i)//5 + i//3)
            ok = True
            break
if not ok:
    if n%3 == 0:
        print(n//3)
    else:
        print(-1)
