def solution(a, b, g, s, w, t):
    end = ((10 ** (9)) * 2) * (10 ** (5)) * 2
    start = 0
    answer = end
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0
        
        for i in range(len(g)):
            _g,_s,_w,_t = g[i], s[i], w[i], t[i]
            move_cnt = mid // (_t * 2)
            if mid % (_t * 2) >= t[i]:
                move_cnt += 1
                
            weight = move_cnt * _w
            gold += _g if (_g < weight) else weight
            silver += _s if (_s < weight) else weight
            total += _g + _s if (_g + _s < weight) else weight

        if total >= a+b and gold >= a and silver >= b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer