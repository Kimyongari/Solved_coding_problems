a,b = input().split()
a = int(a)
b = int(b)
c = int(input())
allmin= (a*60) + b + c
hours = allmin//60
mins = allmin%60
print(f'{hours%24} {mins}')


