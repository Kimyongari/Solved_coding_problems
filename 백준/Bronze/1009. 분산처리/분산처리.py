t = int(input())
d = {1:[1], 2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6], 5:[5], 6:[6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1], 0:[10]}
for _ in range(t):
    a,b = map(int, input().split())
    a = a % 10
    k = b % len(d[a])
    print(d[a][k-1])