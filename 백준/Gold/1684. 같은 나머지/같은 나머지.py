n = int(input())
l = list(map(int, input().split()))
answer = 0
t = max(l)
for i in range(1,t + 1):
    s = set()
    for ele in l:
        s.add(ele%i)
        if len(s) >= 2:
            break
    if len(s) == 1:
        answer = i
print(answer)
