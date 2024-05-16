S = int(input())
a = 0
def sig(n):
    return(n*(n+1)/2)
while S > sig(a):
    a+=1
if sig(a) == S:
    print(a)
else:
    print(a-1)
    