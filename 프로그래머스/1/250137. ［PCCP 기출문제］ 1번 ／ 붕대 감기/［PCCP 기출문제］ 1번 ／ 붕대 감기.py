from collections import deque
def solution(bandage, health, attacks):
    attacks = deque(attacks)
    time = 0
    cnt = 0
    maxhealth = health
    while attacks:
        time += 1
        a = attacks[0]
        if a[0] == time:
            health = health - a[1]
            attacks.popleft()
            cnt = 0
            if health <= 0:
                return -1
        else:
            health += bandage[1]
            cnt += 1
        if cnt == bandage[0]:
            health += bandage[2]
            cnt = 0
        if health >= maxhealth:
            health = maxhealth   
    answer = health
    return answer