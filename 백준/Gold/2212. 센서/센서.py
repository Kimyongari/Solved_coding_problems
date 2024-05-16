n = int(input())
k = int(input())
l = list(map(int,input().split()))
l = sorted(l)
arr = []
for i in range(len(l)-1):
    arr.append(l[i+1] - l[i])
arr = sorted(arr)
print(sum(arr[:len(arr)-(k-1)]))