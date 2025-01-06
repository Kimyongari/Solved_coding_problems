l = []
for _ in range(int(input())):
    l.append(list(map(int, input().split())))
for i in sorted(l, key = lambda x: (x[1], x[0])):
    print(*i)
