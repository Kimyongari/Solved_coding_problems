a = input()
a = int(a)
b = input()
c = []
for i in reversed(b):
    c.append(i)
for j in c:
    print(a*int(j))
    
print(int(b)*a)