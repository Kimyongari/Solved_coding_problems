st = []
for _ in range(int(input())):
    num = int(input())
    if num != 0:
        st.append(num)
    elif num == 0:
        st.pop()
print(sum(st))