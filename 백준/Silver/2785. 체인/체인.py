n = int(input())
l = list(map(int, input().split()))
l = sorted(l)
answer = 0
while l:
    if l[0] >= 1:
        l[0] = l[0] - 1
        l[-1] = l[-1] + l.pop()
        answer += 1
    else:
        l.pop(0)
    if len(l) == 1:
        break

print(answer)