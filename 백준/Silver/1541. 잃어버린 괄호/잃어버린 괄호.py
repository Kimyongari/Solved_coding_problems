l = input()
l = l.split('-')
answer = []
for i in l:
    v = sum(map(int,i.split('+')))
    answer.append(v)
base = answer[0]
minus = sum(answer[1:])
print(base - minus)