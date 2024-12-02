n = int(input())
l = [(n-i)*' ' + '*'*(2*i-1) + ' ' for i in range(1,n+1)] + [' ' + ' ' * (n-i) + '*' * (2*(i-1)-1) + ' ' for i in range(n,1,-1)]
for i in l:
    print(i)
    