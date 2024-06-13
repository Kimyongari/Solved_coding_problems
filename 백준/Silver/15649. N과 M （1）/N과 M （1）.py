from itertools import permutations
m, n = map(int, input().split()) # 6 , 4
l = range(1, m+1)
for p in permutations(l,n):
    print(*p)