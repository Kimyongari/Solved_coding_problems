n = int(input())
nl = set(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))

# ml에 있는 수가 nl에 있는가?
for i in ml:
    if i in nl:
        print(1)
    else:
        print(0)