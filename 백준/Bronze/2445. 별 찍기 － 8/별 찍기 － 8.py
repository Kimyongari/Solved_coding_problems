n = int(input())
l = [i * '*' + ' ' *(2*n-(2*i)) + i * '*' for i in range(1,n)]+[(n-i) * '*' + ' ' * (2*(i)) + (n-i) * '*' for i in range(n)]
for i in l:
    print(i)
