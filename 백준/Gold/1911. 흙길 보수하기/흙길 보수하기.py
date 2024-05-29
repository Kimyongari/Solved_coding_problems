n, l = map(int, input().split())
m = []
for _ in range(n):
    m.append(list(map(int, input().split())))
m = sorted(m, key = lambda x:x[0]) # 1 6, 8 12, 13 17
road = 0
answer = 0
for s,e in m:
    if road <= s:
        road = s
    else:
        s = road
    if (e-s) % l == 0:
        answer += (e-s) // l
        road = e
    else:
        answer += ((e-s) // l) + 1
        road = s + (((e-s) // l) + 1) * l

print(answer)