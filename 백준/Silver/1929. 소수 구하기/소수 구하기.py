import math
M, N = map(int,input().split())
answer = []
def issosu(a):
    d = []
    for i in range(1,int(math.sqrt(a)+1)):
        if a % i == 0:
            d.append(i)
        if len(d) >= 2:
            return False
    return True 
for i in range(M,N+1):
    if i == 1:
        continue
    if issosu(i) == True:
        print(i, end = ' ')

    
