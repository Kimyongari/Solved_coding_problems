from collections import deque

answer = 0
        
for _ in range(int(input())):
    text = input()
    if len(text)%2 == 1:
        continue
    else:
        st = []
        for i in text:
            st.append(i)
            if len(st)>=2 and st[-1] == st[-2]:
                st.pop()
                st.pop()
        if not st:
            answer += 1
print(answer)

                    