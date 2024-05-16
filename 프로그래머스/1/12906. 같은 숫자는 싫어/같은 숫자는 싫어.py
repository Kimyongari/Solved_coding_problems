def solution(arr):
    ans = ['a']
    answer = []
    while arr:
        a = arr.pop()
        if ans[-1] != a:
            ans.append(a)
    ans.reverse()
    return(ans[:len(ans)-1])