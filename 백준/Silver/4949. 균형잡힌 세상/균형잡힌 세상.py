d = {'[' : ']', ']': '', '(' : ')', ')' : ''}
def check(text):
    st = []
    for i in text:
        if i =='(' or i ==')' or i == '[' or i == ']':
            st.append(i)
            if len(st)>=2 and d[st[-2]]==st[-1]:
                st.pop()
                st.pop()
    if st:
        return 'no'
    else:
        return 'yes'

while True:
    text = input()
    if text == '.':
        break
    else:
        print(check(text))