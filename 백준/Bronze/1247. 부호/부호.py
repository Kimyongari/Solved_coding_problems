from sys import stdin
input = stdin.readline
answer = [0,0,0]
for i in range(3):
    A = int(input())
    for j in range(A):
        B = int(input())
        answer[i]=answer[i]+B

for z in answer:
    if z > 0:
        print('+')
    elif z == 0:
        print('0')
    else:
        print('-')
        
