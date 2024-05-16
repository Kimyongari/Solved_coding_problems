def solution(s):
    s = s[1:len(s)-1]
    arr = []
    while s.find("{") != -1:
        l = s.find("{")
        r = s.find("}")
        arr.append(s[l+1:r].split(','))
        s = s[r+1:]
    arr = sorted(arr, key = lambda x : len(x))
    answer = []
    for i in arr:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer