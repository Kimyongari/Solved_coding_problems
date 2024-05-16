n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key = lambda x:(x[1], x[0]))
can = 0
cnt = 0
for start, end in arr:
    if can <= start:
        can = end
        cnt += 1
print(cnt)