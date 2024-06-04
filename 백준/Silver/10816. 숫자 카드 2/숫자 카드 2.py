from collections import Counter
n = int(input())
nl = list(map(int, input().split()))
cnt = Counter(nl)
m = int(input())
ml = list(map(int, input().split()))
for i in ml:
    if i in cnt:
        print(cnt[i])
    else:
        print(0)
    