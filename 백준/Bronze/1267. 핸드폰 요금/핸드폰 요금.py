N = int(input())
list1 = list(map(int, input().split()))
list_Y = []
list_M = []

for i in list1:
    list_Y.append(((i//30)+1)*10)
for i in list1:
    list_M.append(((i//60)+1)*15)

if sum(list_M)>sum(list_Y):
    print('Y' ,sum(list_Y))
elif sum(list_M)==sum(list_Y):
    print('Y M',sum(list_Y))
else:
    print('M',sum(list_M))
    