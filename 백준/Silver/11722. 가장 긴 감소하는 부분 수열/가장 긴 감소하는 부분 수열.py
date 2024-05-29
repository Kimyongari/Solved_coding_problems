n = int(input())
d = [1] * n
a = list(map(int, input().split()))
for i in range(n):
    for j in range(i,n):
        if a[i] > a[j]:
            d[j] = max(d[j], d[i] + 1)

print(max(d))