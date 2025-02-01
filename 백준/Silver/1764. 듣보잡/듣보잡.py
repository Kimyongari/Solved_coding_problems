n,m = map(int, input().split())
듣 = []
보 = []
for _ in range(n):
    듣.append(input())
for _ in range(m):
    보.append(input())

듣 = set(듣)
보 = set(보)
answer = sorted(list(듣.intersection(보)))
print(len(answer))
for i in answer:
    print(i)
