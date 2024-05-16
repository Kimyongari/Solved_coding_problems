n, truck = map(int, input().split())
arr = []
answer = 0
for i in range(int(input())):
    arr.append(list(map(int,input().split())))

arr = sorted(arr, key = lambda x: x[1])
can = [truck] * ((len(arr))+1)
for s,e,cost in arr:
    load = truck
    for i in range(s,e):
        if load > min(cost, can[i]):
            load = min(cost, can[i])
    for i in range(s,e):
        can[i] -= load
    answer += load
print(answer)