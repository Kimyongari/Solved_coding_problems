a,b = input().split()
l_a = len(a)
l_b = len(b)
def diffinder(a,b):
    cnt = 0
    for i in range(len(b)):
        if a[i] != b[i]:
            cnt += 1
    return cnt
if len(a) == len(b):
    print(diffinder(a,b))
else:
    answer = l_b
    for i in range(l_b-l_a+1):
        answer = min(answer, diffinder(a,b[i:l_a+i]))
    print(answer)