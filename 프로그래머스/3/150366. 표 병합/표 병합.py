graph = ['' for _ in range(51)]
graph = [graph[:] for _ in range(51)]
parent = [[(r,c) for c in range(51)] for r in range(51)]

def solution(commands):
    answer = []
    for com in commands:
        l = com.split()
        if l[0] == 'UPDATE':
            update(com)
        elif l[0] == 'MERGE':
            merge(com)
        elif l[0] == 'UNMERGE':
            unmerge(com)
        elif l[0] == 'PRINT':
            answer.append(prin(com))
    return answer

def parentfinder(r, c):
    if parent[r][c] == (r, c):
        return (r, c)
    else:
        pr, pc = parent[r][c]
        return parentfinder(pr, pc)

def update(command):
    l = command.split()
    if len(l) == 4:
        _, r, c, value = l
        r = int(r)
        c = int(c)
        pr, pc = parentfinder(r, c)
        graph[pr][pc] = value
    elif len(l) == 3:
        v1, v2 = l[1], l[2]
        for r in range(1, 51):
            for c in range(1, 51):
                if graph[r][c] == v1:
                    graph[r][c] = v2

def merge(command):
    com = command.split()
    r1, c1, r2, c2 = int(com[1]), int(com[2]), int(com[3]), int(com[4])
    pr1, pc1 = parentfinder(r1, c1)
    pr2, pc2 = parentfinder(r2, c2)
    if (pr1, pc1) == (pr2, pc2):
        return
    value = graph[pr1][pc1] if graph[pr1][pc1] else graph[pr2][pc2]
    parent[pr2][pc2] = (pr1, pc1)
    graph[pr1][pc1] = value
    graph[pr2][pc2] = ''

def unmerge(command):
    l = command.split()
    r, c = int(l[1]), int(l[2])
    pr, pc = parentfinder(r, c)
    v = graph[pr][pc]
    candidates = []
    for _r in range(1, 51):
        for _c in range(1, 51):
            _pr, _pc = parentfinder(_r, _c)
            if (_pr, _pc) == (pr, pc):
                candidates.append((_r, _c))
    for _r, _c in candidates:
        parent[_r][_c] = (_r, _c)
        graph[_r][_c] = ''
    graph[r][c] = v

def prin(command):
    l = command.split()
    r, c = int(l[1]), int(l[2])
    r, c = parentfinder(r, c)
    if graph[r][c]:
        return graph[r][c]
    else:
        return 'EMPTY'
