v,e = map(int, input().split())
d = []
for i in range(e):
    d.append(list(map(int, input().split())))
d = sorted(d, key = lambda x:x[2])
def parent_find(parent,x):
    if parent[x] != x:
        parent[x] = parent_find(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = parent_find(parent,a)
    b = parent_find(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i
answer = 0
for i in d:
    st,ed,cost = i
    if parent_find(parent, st) != parent_find(parent, ed):
        union_parent(parent,st,ed)
        answer += cost
print(answer)