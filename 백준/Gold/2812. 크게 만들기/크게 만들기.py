from collections import deque
n,k = map(int, input().split())
num = deque(list(input()))
q = deque()
while num:
    a = num.popleft()
    if q:
        if q[-1] >= a:
            q.append(a)
        else:
            while k != 0:
                if q and q[-1] < a:
                    q.pop()
                    k -=1
                else:
                    break
            q.append(a)
    else:
        q.append(a)
            
while k != 0:
    q.pop()
    k -= 1
print(int(''.join(q)))
            
    