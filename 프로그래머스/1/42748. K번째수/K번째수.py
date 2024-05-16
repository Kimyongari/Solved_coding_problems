def solution(array, commands):
    answer = []
    for i in commands:
        a, b, c = i
        d = array[a-1:b]
        d = sorted(d)
        answer.append(d[c-1])        
    return answer