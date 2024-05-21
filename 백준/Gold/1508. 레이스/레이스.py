n,m,k = map(int, input().split())
l = list(map(int, input().split()))

start = 1
end = l[-1] - l[0]
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    prev = l[0]
    for i in range(1, k):
        if l[i] - prev >= mid:
            cnt += 1
            prev = l[i]
    if cnt < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

ans = '1'
cnt = 1
prev = l[0]
for i in range(1, k):
	# 심판의 수가 m을 넘지 않으면 심판을 세움.
    if l[i] - prev >= result and cnt < m:
        ans += '1'
        cnt += 1
        prev = l[i]
    else:
        ans += '0'
# 결과출력
print(ans)