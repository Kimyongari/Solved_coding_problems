def solution(genres, plays):
    d = {}
    sum = {}
    l = []
    for i in range(len(genres)):
        if genres[i] not in d:
            d[genres[i]] = [[i, plays[i]]]
            sum[genres[i]] = plays[i]
        else:
            d[genres[i]].append([i, plays[i]])
            sum[genres[i]] += plays[i]       
    sum = sorted(sum.items(), key = lambda x : x[1], reverse = True)
    for i in d:
        d[i] = sorted(d[i], key = lambda x : x[1], reverse = True)
    for i,_ in sum:
        if len(d[i]) >= 2:
            for j in d[i][:2]:
                l.append(j[0])
        else:
            l.append(d[i][0][0])
    answer = l


    return answer