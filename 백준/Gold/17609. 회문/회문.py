from collections import deque
def check(word):
    if len(word) <= 1:
        return True
    while word:
        if word[0] == word[-1]:
            word.pop()
            word.popleft()
        else:
            return False
        if len(word) <= 1:
            return True
n = int(input())
for _ in range(n):
    l = input()
    l = deque(l)
    cnt = 0
    while l:
        if l[0] == l[-1]:
            l.pop()
            l.popleft()
        elif l[0] != l[-1]:
            if check(deque(''.join(l)[:-1])) or check(deque(''.join(l)[1:])):
                print(1)
                break
            else:
                print(2)
                break
        if len(l) <= 1:
            print(0)
            break
            