n = int(input())
l = list(map(int,list(input())))
t = list(map(int,list(input())))

def change(A, B):
    A_copy = A[:]
    press = 0
    for i in range(1, n):
        
        if A_copy[i-1] == B[i-1]:
            continue
        
        press += 1
        for j in range(i-1, i+2):
            if j<n:
                A_copy[j] = 1 - A_copy[j]
    if A_copy == B:
        return press 
    else:
        return 1e9

m1 = change(l,t)
l[0] = 1 - l[0]
l[1] = 1 - l[1]
m2 = change(l,t) + 1
answer = min(m1, m2)
if answer != 1e9:
    print(answer)
else:
    print(-1)