T = int(input())
answer_list = []
for i in range(T):
    me_x,me_y,tar_x,tar_y = map(int,input().split())
    answer_count = 0
    n = int(input())
    for j in range(n):
        c_x,c_y,r = map(int,input().split())
        dis1 = (me_x - c_x)**2 + (me_y - c_y)**2
        dis2 = (tar_x - c_x)**2 + (tar_y - c_y)**2
        pow_r = r**2

        if pow_r > dis1 and pow_r > dis2:
            pass
        elif pow_r > dis1:
            answer_count +=1
        elif pow_r > dis2:
            answer_count +=1
            
    answer_list.append(answer_count)

for i in answer_list:
    print(i)