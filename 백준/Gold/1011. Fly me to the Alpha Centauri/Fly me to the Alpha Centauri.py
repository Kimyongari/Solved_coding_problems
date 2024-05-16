N = int(input())
for i in range(N):
    x, y = map(int,input().split())
    distance = y - x
    n = 1
    while n ** 2 <= distance:
        n += 1
    n = n-1
    a = (n) ** 2
    b = (n+1) ** 2
    l = 2*n - 1
    if distance > a and distance <= a + n:
        l += 1
    if distance > a + n:
        l += 2
    print(l)
    
        
