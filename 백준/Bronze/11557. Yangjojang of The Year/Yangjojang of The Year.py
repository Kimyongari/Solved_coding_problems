a = int(input())

for i in range(a):
    b = int(input())
    name=[]
    consume = 0
    for j in range(b):
        name1,c = input().split()
        if int(c) > consume:
            consume = int(c)
            name = name1
    print(name)
        
        
        
    