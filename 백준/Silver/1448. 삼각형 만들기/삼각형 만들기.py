import sys
N = int(sys.stdin.readline())
line = []
answer = []
for i in range(N):
    a = int(sys.stdin.readline())
    line.append(a)

line = sorted(line,reverse = True)
for i in range(N-2):
        if line[i] < line[i+1] + line[i+2]:
            answer.append(line[i] + line[i+1] + line[i+2])
if len(answer) == 0:
    print(-1)
else:
    print(max(answer))