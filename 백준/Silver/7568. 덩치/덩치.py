n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
answer = [1] * n
for 덩치 in l:
    x1,y1 = 덩치
    cnt = 0
    for i in range(n):
        x2, y2 = l[i]
        if x1 > x2 and y1 > y2:
            answer[i] += 1
for i in answer:
    print(i, end = ' ')