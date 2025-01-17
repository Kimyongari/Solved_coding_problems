s = input()
engs = 'abcdefghijklmnopqrstuvwxyz'
d = {}
for w in engs:
    d[w] = -1

for i in range(len(s)):
    if d[s[i]] == -1:
        d[s[i]] = i
print(*list(d.values()))