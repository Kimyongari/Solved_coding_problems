n = int(input())
a = list(map(int, input().split()))
d = [1] * n
for i in range(n):
    for j in range(i, n):
        if a[j] > a[i]:
            d[j] = max(d[j], d[i] + 1)
print(max(d))
    