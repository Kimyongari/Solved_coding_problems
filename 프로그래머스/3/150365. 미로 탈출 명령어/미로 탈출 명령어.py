def solution(n, m, x, y, r, c, k):
#     dlru
    distance = abs(x-r) + abs(y-c)
    answer = ''
    if distance > k:
        return 'impossible'
    elif (k-distance) % 2 != 0:
        return 'impossible'
    down = max(r-x, 0)
    left = max(y-c, 0)
    right = max(c-y, 0)
    up = max(x-r,0)
    pair = (k - distance) // 2
    print('down :', down, 'left :', left, 'right :', right, 'up :', up)
    
    while len(answer) != k:
        if (down or pair) and x < n:
            answer += 'd'
            if down:
                down -= 1
            else:
                pair -= 1
                up += 1
            x += 1
            
        elif (left or pair) and y > 1:
            answer += 'l'
            if left:
                left -= 1
            else:
                pair -= 1
                right += 1
            y -= 1
        elif (right or pair) and y < m:
            answer += 'r'
            if right:
                right -= 1
            else:
                pair -= 1
                left += 1
            y += 1
        else:
            answer += 'u'
            if up:
                up -= 1
            else:
                pair -= 1
                down += 1
            x -= 1
    print(answer)
    return answer