n = int(input())
num=1
answer = 0
for i in range(1,n+1):
    num *= i
while num%10==0:
    answer += 1
    num = num//10
print(answer)