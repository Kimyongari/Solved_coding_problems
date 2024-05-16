def solution(brown, yellow):
    size = brown + yellow
    for i in range(1,size):
        if size % i == 0:
            h = i
            w = size / h
            if (h-2) * (w-2) == yellow:
                return(w,h)
        
        