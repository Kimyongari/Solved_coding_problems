n = int(input())
l = [' ' * i + '*'*(2*(n-i)-1) + ' ' for i in range(n)]+[' ' * i + '*'*(2*(n-i)-1) + ' ' for i in range(n-1,-1,-1)][1:]
for i in l:
    print(i)
