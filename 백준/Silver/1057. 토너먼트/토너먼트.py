n,a,b = map(int, input().split())
if a > b:
    t = b 
    b = a
    a = t
cnt = 1
while True:
    if (b-a) == 1 and a % 2 == 1:
        break
    a = int(a/2) if a % 2 == 0 else (a//2)+1
    b = int(b/2) if b % 2 == 0 else (b//2)+1
    cnt += 1

print(cnt)