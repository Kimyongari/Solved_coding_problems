from itertools import combinations

n,m = map(int, input().split())
l = list(map(int,input().split()))
answer = 0
for comb in combinations(l,3):
    if answer < sum(comb) <= m:
        answer = sum(comb)
print(answer)