from collections import defaultdict
d = defaultdict(int)
n = int(input())
l = list(map(int, input().split()))

left = 0
right = 0
result = 0
while right < n:
    d[l[right]] += 1
    while len(d) > 2:
        d[l[left]] -= 1
        if d[l[left]] == 0:
            del d[l[left]]
        left += 1
    result = max(result, right - left + 1)
    right += 1
print(result)