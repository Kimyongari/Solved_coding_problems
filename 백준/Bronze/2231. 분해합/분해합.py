n = int(input())
togle = True
for i in range(n):
    j = str(i)
    j = sum(map(int, [num for num in j]))
    if j + i == n:
        print(i)
        togle = False
        break
if togle:
    print(0)
