N = int(input())
for _ in range(N):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    dot_distance = ((((x1-x2)**2)+((y1-y2)**2))**(1/2))
    r_distance = (r1+r2)
    if r1==r2 and x1==x2 and y1==y2:
        print(-1)
    elif abs(r1-r2) < dot_distance < r_distance:
        print(2)
    elif abs(r1 - r2) == dot_distance or (r1 + r2) == dot_distance:  # 내접, 외접일 때
        print(1)
    else:
        print(0)