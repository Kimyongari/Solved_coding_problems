import heapq
t = int(input())
for _ in range(t):
    l = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    answer = 0
    while files:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        s = a + b
        answer += s
        heapq.heappush(files, s)
        if len(files) == 1:
            print(answer)
            break
            