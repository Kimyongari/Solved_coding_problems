from itertools import combinations_with_replacement
n,m = map(int, input().split())
answers = []

l = sorted(list(map(int, input().split())))
for comb in combinations_with_replacement(l,m):
    if comb not in answers:
        answers.append(comb)
for ele in answers:
    print(*ele)
