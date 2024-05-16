N = int(input())
l = list(map(int,input().split()))
m = []
for i in range(3):
    m.append(min([l[5-i], l[i]]))
m.sort()
if N == 1:
    l = sorted(l)
    print(sum(l[:5]))
else:
    one = (((N-2)*(N-1))*4) + ((N-2)*(N-2))
    zero = (N-2) * (N-2) * (N-1)
    two = ((N -1) * 4) + ((N-2) * 4)
    three = 4
    print((one * m[0]) + (two * (m[0]+m[1])) + (three * (m[0] + m[1] + m[2])))