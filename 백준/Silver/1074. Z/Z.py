N, r, c = map(int,input().split())
answer = 0
while N != 0:
    N -= 1
    if r < 2**N and c < 2**N:
        answer = answer + (4**N*0)
    elif r < 2**N and c >= 2**N:
        c-= (2**N)
        answer = answer + (4**N*1)
    elif r >= 2**N and c < 2**N:
        r-= (2**N)
        answer = answer + (4**N*2)
    else: 
        r-= (2**N)
        c-= (2**N)
        answer = answer + (4**N*3)
print(answer)