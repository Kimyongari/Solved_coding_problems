# 10개 > 2 / 17, 26, 35 
# 11개 > 2 / 18, 27, 36
# 12개 > 2 / 19, 28, 37, 46

#  10개 > 4
#  9개 > 3
#  8개 > 3 
#  7개 > 2개
#  6개 > 2개  15,24
n = int(input())
if n < 6:
    print(0)
else:
    answer = 0
    for i in range(2, n-3, 2):
        candy = n - i
        answer += (candy // 2) - 1
    print(answer)
        