
def solution(numbers, target):
    answer = 0
    queue = []
    queue.append([0, numbers[0]])
    queue.append([0, -numbers[0]])
    while queue:
        idx, a = queue.pop()
        if idx == len(numbers)-1:
            if a == target:
                answer +=1
        else:
            queue.append([idx+1, a - numbers[idx+1]])
            queue.append([idx+1, a + numbers[idx+1]])
    return answer