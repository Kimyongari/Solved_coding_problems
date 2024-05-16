def solution(s):
    s = list(s)
    s = sorted(s, reverse = True)

    return ''.join(s)