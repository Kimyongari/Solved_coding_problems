def solution(nums):
    can = len(nums)/2
    c = []
    for i in nums:
        if i not in c:
            c.append(i)
    if len(c) >= can:
        answer = can
    else:
        answer = len(c)
    return answer