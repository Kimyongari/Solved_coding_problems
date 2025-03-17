n = int(input())
target = 'IO' * (n) + 'I'
m = int(input())
s = input()
l = len(target)
answer = 0
for i in range(0,m-l+1):
    if s[i:i+l] == target:
        answer += 1
print(answer)