n = int(input())
m = int(input())
s = input()
cnt = 0
answer = 0
pointer = 0
while pointer < m-1:
    if s[pointer:pointer+3] == 'IOI':
        pointer += 2
        cnt += 1
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        pointer += 1
        cnt = 0

print(answer)