n, m = map(int, input().split())
knowlst = set(input().split()[1:])
parties = []

for i in range(m):
    parties.append(set(input().split()[1:]))

for i in range(m):       
    for people in parties:
        if people & knowlst:
            knowlst = knowlst | people
cnt = 0
for people in parties:
    if people & knowlst:
        continue
    else:
        cnt += 1
print(cnt)