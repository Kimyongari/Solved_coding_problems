import sys
input = sys.stdin.readline
st = []
for _ in range(int(input())):
    order = input().split()
    if order[0] == 'push':
        st.append(int(order[-1]))
    elif order[0] == 'top':
        if st:
            print(st[-1])
        else:
            print(-1)
    elif order[0] == 'pop':
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop())
    elif order[0] == 'size':
        print(len(st))
    elif order[0] == 'empty':
        if st:
            print(0)
        else:
            print(1)
    