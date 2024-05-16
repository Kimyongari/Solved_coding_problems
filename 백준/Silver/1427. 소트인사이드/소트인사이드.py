N = input()
answer = []
for i in N:
    answer.append(i)
answer.sort(reverse=True)
print(''.join(answer))