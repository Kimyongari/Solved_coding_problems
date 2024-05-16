import sys
input = sys.stdin.readline
n,m = map(int,input().split())
l = []
for i in range(m):
    l.append(list(map(int, input().split())))
parent = [0] * n
for i in range(n):
    parent[i] = i
    
def parent_find(parent,x):
    if parent[x] == x:
        return x
    parent[x] = parent_find(parent,parent[x])
    return parent[x]

def union_parent(parent,f,s):
    a = parent_find(parent,f)
    b = parent_find(parent,s)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
answer = []
for i in range(len(l)):
    s,e = l[i]
    if parent_find(parent,s) == parent_find(parent,e):
        answer.append(i+1)
    else:
        union_parent(parent,s,e)

if answer:
    print(answer[0])
else:
    print(0)