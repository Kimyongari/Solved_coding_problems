from itertools import combinations

n,c = map(int, input().split())
l = list(map(int, input().split()))
l1 = l[:n//2]
l2 = l[n//2:]

a,b = [], []
for i in range(len(l1)+1):
    for comb in combinations(l1, i):
        s = sum(comb)
        a.append(s)
for i in range(len(l2)+1):
    for comb in combinations(l2, i):
        s = sum(comb)
        b.append(s)

a.sort()
answer = 0
for target in b:
    if target > c:
        continue
    start = 0
    end = len(a)-1
    while start <= end:
        mid = (start+end)//2
        if target + a[mid] > c:
            end = mid-1
        else:
            start = mid + 1
    answer += end + 1

print(answer)

