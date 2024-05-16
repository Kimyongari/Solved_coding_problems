def dfs(num, tree):
    tree[num] = -2
    for i in range(len(tree)):
        if num == tree[i]:
            dfs(i, tree)

n = int(input())
tree = list(map(int, input().split()))
erase = int(input())
count = 0

dfs(erase, tree)
count = 0
for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        count += 1
print(count)