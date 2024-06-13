n = int(input())
x = list(map(int, input().split()))
s = set(sorted(x))
d = {}
tier = 0
for i in sorted(list(s)):
    d[i] = tier
    tier += 1
for i in x:
    print(d[i], end = ' ')