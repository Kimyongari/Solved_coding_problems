a = input()
b = []
c = []
d = []
for i in range(int(a)):
    d.append(input().split())
for i in range(len(d)):
    b.append(d[i][0])
    c.append(d[i][1])
for i in range(int(a)):
    print(f"Case #{i+1}:",int(b[i])+int(c[i]))