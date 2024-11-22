a,b,n,w = map(int, input().split())

# 양염소 전체가 n마리이고, 어제 하루 동안 소비한 전체 사료의 양이 w그램
groups = []
answer = []
for i in range(1,n):
    groups.append([i, n-i])

for group in groups:
    a1,b1 = group
    if a*a1 + b*b1 == w:
        answer.append(group)
if len(answer) == 1:
    print(*(answer[0]))
else:
    print(-1)