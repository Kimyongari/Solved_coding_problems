import sys
input = sys.stdin.readline
n,c = map(int, input().split())
l = []
answer = 0
for _ in range(n):
    l.append(int(input()))
l = sorted(l)
k = 0
start = 1
end = l[-1] - l[0]
while start <= end:
    mid = (start + end) // 2
    now = l[0]
    cnt = 1
    for i in range(1,n):
        if l[i] - now >= mid:
            now = l[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)