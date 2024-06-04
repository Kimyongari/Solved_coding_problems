n, m = map(int,input().split())
l = list(map(int, input().split()))
start = 1
end = max(l)
mid = (start + end) // 2
while start <= end:
    leng = 0
    for i in l:
        if i > mid:
            leng += i - mid
    if leng >= m: # 길면 > mid를 올린다
        start = mid + 1
        mid = (start + end) // 2
    else: # 짧으면 > mid를 내린다
        end = mid - 1
        mid = (start + end) // 2
print(mid)