A,B = map(int, input().split())
a,b,c = 1, 2*A, B

x1 = int((-b + ((b**2-4*a*c)**0.5))/2)
x2 = int((-b - ((b**2-4*a*c)**0.5))/2)

if x1==x2:
    print(x1)
else:
    print(*sorted([x1,x2]))

