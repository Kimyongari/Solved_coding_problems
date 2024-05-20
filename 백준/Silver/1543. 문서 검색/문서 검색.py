l = input()
word = input()
start, end = 0, len(word)
answer = 0
while end <= len(l):
    if l[start:end] == word:
        answer += 1 
        start = end
        end = start + len(word)
    else:
        start += 1
        end += 1

print(answer)