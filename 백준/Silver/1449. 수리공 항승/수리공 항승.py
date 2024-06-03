n,l = map(int, input().split())
m = list(map(int, input().split()))
m = sorted(m)
s = 0
cnt = 0
for i in m:
    if s < i + 0.5:
        s = i - 0.5 + l
        cnt += 1
print(cnt)