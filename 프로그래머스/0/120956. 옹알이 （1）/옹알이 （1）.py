from collections import deque
def solution(babbling):
    can = deque(['aya', 'ye', 'woo', 'ma'])
    answer = 0
    for word in babbling:
        for i in can:
            if word.find(i) != -1:
                word = word.replace(i, ' ', 1)
                print(word)
        d = ''
        for i in word:
            if i == ' ':
                continue
            else:
                d += i
        if d == '':
            answer += 1
            
    return answer