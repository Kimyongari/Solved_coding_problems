N=int(input())
n=[]
for i in range(0, N):
    n.append(input())

n=sorted(list(set(n)))
n=sorted(n, key=len)
for itr in n:
    print(itr)