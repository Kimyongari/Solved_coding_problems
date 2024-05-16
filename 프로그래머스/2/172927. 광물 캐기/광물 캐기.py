from collections import deque
def solution(picks, minerals):

    blocks = []
    l = len(minerals)
    if sum(picks)*5 < l:
        minerals = minerals[:sum(picks)*5]
        

    for i in range(l//5):
        blocks.append(minerals[5*i:5*(i+1)])
    blocks.append(minerals[5*(i+1):])
    d = {'diamond' : 25, 'iron' : 5, 'stone' : 1}
    dia = {'diamond' : 1, 'iron' : 1, 'stone' : 1}
    iron = {'diamond' : 5, 'iron' : 1, 'stone' : 1}
    stone = { 'diamond' : 25, 'iron' : 5, 'stone' : 1}
    for i in range(len(blocks)):
        w = 0
        for j in blocks[i]:
            w += d[j]
        blocks[i].append(w)
    blocks = deque(sorted(blocks, key = lambda x : x[-1], reverse = True))
    print(blocks)
    result = 0
    while blocks:
        b = blocks.popleft()
        b.pop()
        if picks == [0,0,0]:
            return result
        if picks[0] != 0:
            for i in b:
                result += dia[i]
            picks[0] -= 1
        elif picks[1] != 0:
            for i in b:
                result += iron[i]
            picks[1] -= 1
        else:
            for i in b:
                result += stone[i]
            picks[2] -= 1
    return result