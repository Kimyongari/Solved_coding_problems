n = int(input())

# a^2 + n > b^2
answer = 0
for a in range(1,500):
    for b in range(1,500):
        if a**2 == b**2+n:
            answer += 1
print(answer)
