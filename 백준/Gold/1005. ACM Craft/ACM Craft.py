from collections import deque
import sys
input = sys.stdin.readline
T=int(input())
 
for _ in range(T):
    N,K=map(int,input().split())
    time=[0]+list(map(int,input().split()))
    seq=[[] for _ in range(N+1)]
    inDegree=[0 for _ in range(N+1)]
    DP=[0 for _ in range(N+1)]
 
    for _ in range(K):
        a,b=map(int,input().split())
        seq[a].append(b)
        inDegree[b]+=1
    q = deque()
    for i in range(1,N+1):
        if inDegree[i]==0:
            q.append(i)
            DP[i]=time[i]
    while q:
        a=q.popleft()
        for i in seq[a]:
            inDegree[i]-=1
            DP[i]=max(DP[a]+time[i],DP[i])
            if inDegree[i]==0:
                q.append(i)
 
 
    ans=int(input())
    print(DP[ans])