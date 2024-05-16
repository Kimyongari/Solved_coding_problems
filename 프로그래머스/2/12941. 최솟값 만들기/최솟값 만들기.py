from collections import deque
def solution(A,B):
    answer = 0 
    A = sorted(A)
    B = sorted(B, reverse = True)
    while A:
        answer += (A.pop()) * (B.pop())
    

    return answer