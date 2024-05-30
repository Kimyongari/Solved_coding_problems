import sys
input = sys.stdin.readline
n = int(input())
p = []
for i in range(n):
    p.append(int(input()))
p = sorted(p)
answer = [abs((i+1) - j) for i,j in enumerate(p)]
print(sum(answer))