from itertools import combinations_with_replacement
n,m = map(int, input().split())

l = [i+1 for i in range(n)]
for comb in combinations_with_replacement(l,m):
    print(*comb)
