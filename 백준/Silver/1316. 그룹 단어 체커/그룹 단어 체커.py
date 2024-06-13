n = int(input())
answer = 0
for _ in range(n):
    word = input()
    l = []
    now = ''
    for i in word:
        if i not in l or i == now:
            now = i
            l.append(i)
        else:
            answer -= 1
            break
    answer += 1
print(answer)