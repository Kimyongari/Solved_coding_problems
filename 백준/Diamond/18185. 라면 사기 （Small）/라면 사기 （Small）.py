N = int(input())
l = list(map(int, input().split()))
l += [0,0]
cost = 0
def buy1(n): # 1개 살 경우
    global cost
    cost += 3 * l[n]
    l[n] = 0

def buy2(n): # 2개 살 경우
    global cost
    m = min(l[n:n+2])
    l[n] -= m
    l[n+1] -= m
    cost += 5 * m    

def buy3(n): # 3개 살 경우
    global cost
    m = min(l[n:n+3])
    l[n] -= m
    l[n+1] -= m
    l[n+2] -= m
    cost += 7 * m

for i in range(len(l)-2):
    if l[i+1] > l[i+2]:
        m = min(l[i], l[i+1]-l[i+2])
        l[i] -= m
        l[i+1] -= m        
        cost += 5 * m
        buy3(i)
        buy1(i)
    else:
        buy3(i)
        buy2(i)
        buy1(i)

print(cost)