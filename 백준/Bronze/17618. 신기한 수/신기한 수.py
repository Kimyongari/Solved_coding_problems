N = input()
count = 0
def S(m):
    list(m)
    h = 0
    for i in range(len(m)):
        h += int(m[i])
    return h
for i in range(1,int(N)+1):
    if i % S(str(i)) == 0:
        count += 1
print(count)