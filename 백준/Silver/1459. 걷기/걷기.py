x, y, w, s = map(int, input().split()) 
# w 가로세로, s 대각선
if s >= w * 2:
    print((x * w) + (y * w))
elif w <= s <= 2*w:
    cross = min(x,y)
    x, y = x - cross, y - cross
    print(cross * s + max(x,y) * w)
else:
    if (x+y) % 2 == 1:
        cross = max(x,y) - 1
    else:
        cross = max(x,y)
    x, y = x - cross, y - cross
    print(cross * s + max(x,y) * w)
