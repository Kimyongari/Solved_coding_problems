for i in range(1,int(input())+1):
    l = list(map(int,input().split()))
    print(f'Case #{i}: {l[0]} + {l[1]} = {sum(l)}')
