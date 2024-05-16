def solution(sides):
    max_ = max(sides)
    min_ = min(sides)
    case1 = len(range(max_ - min_ + 1, max_ + 1))
    case2 = len(range(max_ + 1, max_ + min_))
    return case1 + case2