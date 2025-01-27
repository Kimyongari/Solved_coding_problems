import sys

input = sys.stdin.readline
ans = int(1e9)
glevel = 0
block = []
N,M,B = map(int, input().split())
for _ in range(N):
    block.append(list(map(int, input().split())))
for i in range(257): #땅 높이
    use_block = 0
    take_block = 0
    for x in range(N):
        for y in range(M):
            if block[x][y] > i:
                take_block += block[x][y] - i
            else:
                use_block += i - block[x][y]

    if use_block > take_block + B:
        continue

    count = take_block * 2 + use_block

    if count <= ans:
        ans = count
        glevel = i

print(ans, glevel)