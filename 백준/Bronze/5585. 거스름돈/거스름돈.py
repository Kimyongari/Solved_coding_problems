n = int(input())
l = [1, 5, 10, 50, 100, 500]
rest = 1000 - n
l = sorted(list(filter(lambda x: x <= rest, l)), reverse = True)
cnt = 0
for i in l:
    cnt += rest // i
    rest %= i
print(cnt)