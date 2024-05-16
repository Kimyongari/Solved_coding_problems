N = int(input())
if  N < 100:
    print(N)
else:
    count = 99
    for i in range(100,N+1):
        d = list(str(i))
        m1 = int(d[0]) - int(d[1])
        m2 = int(d[1]) - int(d[2])
        if m1 == m2:
            count += 1
    print(count)