
def solution(people, limit):
    people = sorted(people)
    f, e = 0, len(people) - 1
    cnt = 0
    while f <= e:
        if people[f] + people[e] <= limit:
            f += 1
            e -= 1
            cnt += 1
        else:
            e -= 1
            cnt += 1
    return cnt
        
