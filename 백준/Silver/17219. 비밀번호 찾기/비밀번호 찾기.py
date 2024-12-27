
n,m = map(int,input().split())
d = {}

for _ in range(n):
    link,password = input().split()
    d[link] = password
for _ in range(m):
    print(d[input()])

