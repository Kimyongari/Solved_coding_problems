from collections import defaultdict
for _ in range(int(input())):
    d = defaultdict(list)
    for __ in range(int(input())):
        a,b = input().split()
        d[b].append(a)
    answer = 1
    for k in d:
        answer *= len(d[k])+1
    print(answer-1)
