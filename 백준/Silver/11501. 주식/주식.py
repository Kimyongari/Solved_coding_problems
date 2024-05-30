t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.reverse()
    m = l[0]
    answer = 0
    for i in range(1,len(l)):
        if m > l[i]:
            answer += m - l[i]
        else:
            m = l[i]
    print(answer)