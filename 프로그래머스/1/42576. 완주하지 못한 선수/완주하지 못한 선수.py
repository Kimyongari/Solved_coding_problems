def solution(participant, completion):
    shash = 0
    d = {}
    for part in participant:
        d[hash(part)] = part
        shash += hash(part)
        
    for comp in completion:
        shash -= hash(comp)
    return d[shash]