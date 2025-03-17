import sys
input = sys.stdin.readline
import math
t = int(input())

def finder(x,y):
    cnt = 1
    while True:
        if math.gcd(x,y) != 1:
            gongyaksu = math.gcd(x,y)
            x = int(x/gongyaksu)
            y = int(y/gongyaksu)
            cnt *= gongyaksu
        else:
            cnt = x*y*cnt
            break
    return cnt


for _ in range(t):
    m,n,x,y = map(int, input().split())
    answer = -1
    flag = False
    cnt = finder(m,n)
    x_zone = set()
    y_zone = set()
    for i in range(cnt//m):
        x_zone.add(m*i+x)
    for i in range(cnt//n):
        _y = n*i+y
        if _y in x_zone:
            answer = _y
            break
    print(answer)
    