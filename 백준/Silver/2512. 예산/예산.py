n = int(input())
l = list(map(int, input().split()))
cost = int(input())
start = 0
end = max(l)
while start < end:
    mid = (start + end) // 2
    can_cost = 0
    for i in l:
        can_cost += mid if i > mid else i
    if can_cost <= cost:
        start = mid + 1
    else:
        end = mid - 1
can_cost = 0
for i in l:
    can_cost += start if i > start else i
if can_cost > cost:
    print(start - 1)
else:
    print(start)