k = int(input())
a = 1
while a < k:
    a *= 2 
ans = a
me = 0
cnt = 0
if a == k:
    print(ans, 0)
else:
    while k > 0:
        cnt += 1
        a = a // 2
        if k-a >=0:
            k -= a
        else:
            continue
    print(ans, cnt)
    
