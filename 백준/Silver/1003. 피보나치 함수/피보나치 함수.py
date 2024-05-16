fibo = [0]*41
def fibonachi(n):
    if n == 0:
        fibo[n] = 0
        return 0
    elif n == 1:
        fibo[n] = 1
        return 1
    elif fibo[n] != 0:
        return fibo[n]
    else:
        fibo[n] = fibonachi(n-1)+fibonachi(n-2)
        return fibo[n]
K = int(input())
answer = []
for _ in range(K):
    N = int(input())
    if N == 0:
        answer.append(0)
        answer.append(1)
    elif N == 1:
        answer.append(1)
        answer.append(0)
    else:
        answer.append(fibonachi(N))
        answer.append(fibonachi(N-1))
for i in range(K):
    print(answer[(2*i)+1],answer[2*i])
    
    