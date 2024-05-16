1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
def find_all_mixture(n, k):
    if n==None:
        return [k, -k]
    return [n-k, n+k, n//k, n*k]

def solution(N, number):
    if N==number:
        return 1

    dp = []
    dp.append([None])
    dp.append([N,-N])
    for i in range(1,8):
        temp = []
        for element in dp[i]:
            temp.extend(find_all_mixture(element, N))

        multipler = 11
        for k in range(i):
            for element in dp[i - 1 - k]:
                temp.extend(find_all_mixture(element, N*multipler))
            multipler += 10 ** (k+2)

        if number in temp:
            return i+1
        dp.append(temp)

    return -1