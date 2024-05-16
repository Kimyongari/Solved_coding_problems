def solution(n, m):
    num = 0
    for i in range(1, min(n,m) + 1):
        if n%i == 0 and m%i ==0:
            num = i
    num2 = int(n * m / num)
    answer = [num,num2]
    return answer