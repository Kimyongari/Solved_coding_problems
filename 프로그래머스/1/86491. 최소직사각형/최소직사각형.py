def solution(sizes):
    d = []
    for i in sizes:
        a,b = i
        d.append(a)
        d.append(b)
    l = max(d)
    h = min(d)
    for i in sizes:
        if min(i) >= h:
            h = min(i)
    
    return l * h