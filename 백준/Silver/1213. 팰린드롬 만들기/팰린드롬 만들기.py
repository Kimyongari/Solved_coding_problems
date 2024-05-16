from collections import Counter
en = input()
count = Counter(en)
odd_num = 0
answer = ''
half = ''
for i in count:
    if count[i] % 2 != 0:
        odd_num += 1
        half = i
if odd_num >= 2:
    print("I'm Sorry Hansoo")
    import sys
    sys.exit()
else:
    for i in sorted(count):
        answer = answer + i * (int(count[i]/2))
if odd_num == 1:
    a_answer = answer + half
    for i in sorted(answer,reverse = True):
        a_answer = a_answer + i
    print(a_answer)
else : 
    for i in sorted(answer, reverse = True):
        answer = answer + i
    print(answer)