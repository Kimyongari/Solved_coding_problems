T = int(input())
for t in range(T):
    score = 0
    cnt = 0
    
    ox = input()
    for i in range(len(ox)):
        if ox[i] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
        
    print(score)