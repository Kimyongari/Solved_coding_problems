import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    l, a = a[0], a[1:]
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    if max(d.values()) * 2 > l:
        for i in d:
            if d[i] == max(d.values()):
                print(i)
                break
    else:
        print('SYJKGW')