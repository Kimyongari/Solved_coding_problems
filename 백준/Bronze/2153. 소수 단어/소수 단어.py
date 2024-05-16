import math
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
    'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dic = {}
for i,j in enumerate(l):
    dic[j] = i+1
n = input()
def isprime(a):
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True
all = 0
for i in n:
    all += dic[i]
if isprime(all) == True:
    print('It is a prime word.')
if isprime(all) == False:
    print('It is not a prime word.')
