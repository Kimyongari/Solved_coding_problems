from itertools import product
def solution(word):
    w = ['A','E','I','O','U']
    l = []
    for i in range(1,6):
        for j in list(product(w, repeat = i)):
            tmp = ''.join(j)
            l.append(tmp)
    l.sort()
    return (l.index(word) + 1)

