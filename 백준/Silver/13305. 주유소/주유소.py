n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
cheap = [cost[0]]
cost = cost[1:]
for i in range(len(cost)):
    if cost[i] < cheap[i]:
        cheap.append(cost[i])
    else:
        cheap.append(cheap[i])
cheap = cheap[:len(cheap)-1]
result = 0
for i in range(len(cheap)):
    result += cheap[i] * distance[i]

print(result)
