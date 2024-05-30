from collections import deque
s = deque(list(input()))
t = deque(list(input()))
while True:
    if len(t) == len(s) and t != s:
        print(0)
        break
    if t == s:
        print(1)
        break
        
    if t[-1] == 'A':
        t.pop()
    else:
        t.reverse()
        t.popleft()


