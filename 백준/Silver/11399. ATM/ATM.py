n = int(input())
l = list(map(int, input().split()))
l = sorted(l)
answer = 0
for i in range(len(l)):
    answer += sum(l[:len(l)-i])
print(answer)