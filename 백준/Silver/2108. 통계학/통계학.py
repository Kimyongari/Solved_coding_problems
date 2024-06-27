from collections import Counter
import sys
input = sys.stdin.readline
arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
e = int(round(sum(arr)/len(arr),0))
m = sorted(arr)[len(arr)//2]
me = Counter(arr)
r = max(arr) - min(arr)

if e == 0:
    print(0)
else:
    print(e)
    
print(m)

d = []
for i in me:
    d.append([i, me[i]])
d = sorted(d, key = lambda x: (x[1],-x[0]), reverse = True)
if n == 1:
    print(d[0][0])
elif n >= 2:
    if d[0][1] == d[1][1]:
        print(d[1][0])
    else:
        print(d[0][0])
        
print(r)

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이