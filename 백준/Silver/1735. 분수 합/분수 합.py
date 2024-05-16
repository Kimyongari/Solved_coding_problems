def gcd(a,b):
    while b>0:
        a,b = b, a % b
    return a
third = []
fisrt = list(map(int,input().split()))
second = list(map(int,input().split()))

third.append(fisrt[0]*second[1]+fisrt[1]*second[0])
third.append(fisrt[1]*second[1])
print(int(third[0]/ gcd(third[0],third[1])),int(third[1] / gcd(third[0],third[1])))